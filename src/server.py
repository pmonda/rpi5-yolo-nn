# receiver.py
import socket
import pickle
import signal
import sys
import time
from tiny_yolo import *
from client import model, split_idx, img, sized
from utils import *

UDP_IP = "0.0.0.0"
UDP_PORT = 5005
TIMEOUT = 10
MAX_RETRIES = 3

def signal_handler(sig, frame):
    print("\nShutting down server...")
    sock.close()
    sys.exit(0)

def split_model(model, split_idx):
    # Use model.cnn instead of model.module_list
    part2 = nn.Sequential(*list(model.cnn.children())[split_idx:])
    return part2

def get_part2(intermediate_tensor, part2):
    with torch.no_grad():
        feature_out = part2(intermediate_tensor)
        return feature_out

# Set up signal handler for graceful shutdown
signal.signal(signal.SIGINT, signal_handler)

try:
    device = "cpu"  # Force CPU usage
    print(f"Using device: {device}")
    model = model.to(device)  # Move entire model to CPU
    model.eval()  # Ensure model is in evaluation mode
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    sock.settimeout(TIMEOUT)
    print(f"Server listening on {UDP_IP}:{UDP_PORT}")
    print("Press Ctrl+C to stop the server")

    while True:
        try:
            print("Waiting for data...")
            data, addr = sock.recvfrom(1024)
            total_packets = int(data.decode())
            print(f"Expecting {total_packets} packets...")
            
            # Send acknowledgment for metadata
            sock.sendto(b"ACK", addr)
            
            received_data = bytearray()
            received_packets = set()
            start_time = time.time()
            
            while len(received_packets) < total_packets:
                try:
                    # Receive packet with sequence number
                    packet_data, _ = sock.recvfrom(4096 + 4)  # Extra 4 bytes for seq num
                    seq_num = int.from_bytes(packet_data[:4], 'big')
                    packet = packet_data[4:]
                    
                    if seq_num not in received_packets:
                        received_packets.add(seq_num)
                        received_data.extend(packet)
                        
                        # Send acknowledgment
                        sock.sendto(seq_num.to_bytes(4, 'big'), addr)
                        
                        if len(received_packets) % 100 == 0:
                            print(f"Received {len(received_packets)}/{total_packets} packets")
                
                except socket.timeout:
                    print("Packet timeout, waiting for retransmission...")
                    continue
            
            print("Deserializing data...")
            tensor = pickle.loads(received_data)
            elapsed = time.time() - start_time
            print(f"Transfer complete in {elapsed:.2f} seconds")
            print(f"Tensor shape: {tensor.shape}")
            print(f"Tensor device: {tensor.device}")
            print(f"Tensor type: {tensor.dtype}")
            
            # Process on CPU
            part2 = split_model(model, split_idx)
            part2 = part2.cpu()
            final_tensor = get_part2(tensor, part2)
           
            with torch.no_grad():
                output = part2(tensor)
                
                # Reshape output to get class probabilities
                # YOLO output shape is [batch, anchors * (5 + num_classes), grid_h, grid_w]
                batch_size, _, grid_h, grid_w = output.shape
                num_classes = 20  # VOC dataset has 20 classes
                
                # Get class probabilities across all grid cells
                class_probs = output.view(batch_size, 5, 5 + num_classes, grid_h, grid_w)[:, :, 5:, :, :]
                # Average probabilities across anchors and grid cells
                class_probs = class_probs.mean(dim=[1, 3, 4])
                
                # Get top prediction
                confidence, class_idx = torch.max(class_probs[0], dim=0)
                
                # Load class names and print prediction
                class_names = load_class_names('voc.names')
                print("\nClassification Result:")
                print(f"Class: {class_names[class_idx]}")
                print(f"Confidence: {confidence:.2f}")
            
            print("Processing complete")
            # Send the final tensor back to client if needed
            # ... add code here for sending results back ...
        except socket.timeout:
            print("Timeout waiting for initial data")
            continue
        except Exception as e:
            print(f"Error processing data: {e, type(e)}")
            continue

except Exception as e:
    print(f"Server error: {e}")
finally:
    sock.close()
