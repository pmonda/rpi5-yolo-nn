import socket
import torch
import pickle


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
img_tensor = image2torch(sized)
print(get_part1(img_tensor, part1))
# Prepare tensor
tensor = torch.randn(3, 224, 224)  # Example tensor
data_bytes = pickle.dumps(tensor)  # Serialize the tensor

# Setup UDP socket
UDP_IP = "192.168.1.205"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Chunk the data
MAX_PACKET_SIZE = 4096
total_packets = (len(data_bytes) - 1) // MAX_PACKET_SIZE + 1

# Send metadata
sock.sendto(str(total_packets).encode(), (UDP_IP, UDP_PORT))

# Send each chunk
for i in range(total_packets):
    start = i * MAX_PACKET_SIZE
    end = start + MAX_PACKET_SIZE
    sock.sendto(data_bytes[start:end], (UDP_IP, UDP_PORT))
