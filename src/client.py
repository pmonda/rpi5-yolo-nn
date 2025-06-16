import socket
import torch
import pickle
import time

from tiny_yolo import *
from PIL import Image
from utils import *

def split_model(model, split_idx):
    # Use model.cnn instead of model.module_list
    part1 = nn.Sequential(*list(model.cnn.children())[:split_idx])
    return part1

def get_part1(img_tensor, part1):
    with torch.no_grad():
        feature_out = part1(img_tensor)
        return feature_out

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = TinyYoloNet()
model.float()
model.load_weights('../model_weights/yolov2-tiny-voc.weights')
model.eval()

# # Inspect layer list to choose split index
# for idx, layer in enumerate(model.cnn):
#     print(f"{idx}: {layer.__class__.__name__}")

# Choose split point that does NOT include RegionLoss
split_idx = len(model.cnn)//2  # All layers up to but not including RegionLoss
part1 = split_model(model, split_idx)
# part1.cuda()

# Load and prepare image
img = Image.open('pmh2mmc4.png').convert('RGB')
sized = img.resize((416, 416))

import warnings

warnings.filterwarnings("ignore", category=UserWarning, message="TypedStorage is deprecated.*")

img_tensor = image2torch(sized)
intermediate_tensor = get_part1(img_tensor, part1)

# Print tensor info before sending
print(f"Tensor shape: {intermediate_tensor.shape}")
print(f"Tensor device: {intermediate_tensor.device}")
print(f"Tensor type: {intermediate_tensor.dtype}")
print(intermediate_tensor)

# Prepare tensor
data_bytes = pickle.dumps(intermediate_tensor)
print(f"Serialized data size: {len(data_bytes) / (1024*1024):.2f} MB")

# Setup UDP socket with timeout
UDP_IP = "192.168.1.205"
UDP_PORT = 5005
TIMEOUT = 5  # 5 second timeout
MAX_RETRIES = 3

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(TIMEOUT)

    MAX_PACKET_SIZE = 4096
    total_packets = (len(data_bytes) - 1) // MAX_PACKET_SIZE + 1
    print(f"Splitting data into {total_packets} packets")

    # Send metadata and wait for acknowledgment
    retries = 0
    while retries < MAX_RETRIES:
        sock.sendto(str(total_packets).encode(), (UDP_IP, UDP_PORT))
        try:
            ack, _ = sock.recvfrom(1024)
            if ack == b"ACK":
                break
        except socket.timeout:
            retries += 1
            print(f"Metadata retry {retries}/{MAX_RETRIES}")
    
    if retries == MAX_RETRIES:
        raise Exception("Failed to establish connection")

    print("Starting transfer...")
    start_time = time.time()
    unacked_packets = set(range(total_packets))
    
    while unacked_packets:
        for seq_num in list(unacked_packets):
            start = seq_num * MAX_PACKET_SIZE
            end = start + MAX_PACKET_SIZE
            packet = seq_num.to_bytes(4, 'big') + data_bytes[start:end]
            sock.sendto(packet, (UDP_IP, UDP_PORT))
            
            try:
                ack, _ = sock.recvfrom(4)
                acked_seq = int.from_bytes(ack, 'big')
                if acked_seq in unacked_packets:
                    unacked_packets.remove(acked_seq)
                    if len(unacked_packets) % 100 == 0:
                        progress = ((total_packets - len(unacked_packets)) / total_packets) * 100
                        print(f"Progress: {progress:.1f}% ({total_packets - len(unacked_packets)}/{total_packets} packets)")
            except socket.timeout:
                continue

    elapsed = time.time() - start_time
    print(f"Transfer complete in {elapsed:.2f} seconds")
    print(f"Average speed: {(len(data_bytes) / (1024*1024)) / elapsed:.2f} MB/s")

except socket.timeout:
    print("Socket timeout occurred")
except Exception as e:
    print(f"Error during transfer: {e}")
finally:
    sock.close()
    print("Socket closed")
