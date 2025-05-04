import cv2
import socket
from split_model_utils import *

# Setup
model = YOLO('yolov8n.pt')
model = attach_hooks(model)

pc_ip = '192.168.1.205' 
port = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Load test image
img = cv2.imread('test.jpg')
img = cv2.resize(img, (640, 640))
img_tensor = torch.from_numpy(img).permute(2, 0, 1).unsqueeze(0).float() / 255

# Run part of the model
_ = model(img_tensor)

# Extract features
tensor = intermediate_outputs["conv2"]
data, shape = compress_tensor(tensor)

# Send shape info
sock.sendto(str(shape).encode(), (pc_ip, port))
# Send compressed data in chunks
for i in range(0, len(data), 4096):
    sock.sendto(data[i:i+4096], (pc_ip, port))

print("Sent tensor with shape", shape)
