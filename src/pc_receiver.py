import socket
from split_model_utils import *
from ultralytics import YOLO
import ast

# Setup
model = YOLO('yolov8n.pt')
model = attach_hooks(model)

port = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", port))

# Step 1: Receive shape
shape_data, _ = sock.recvfrom(1024)
shape = ast.literal_eval(shape_data.decode())

# Step 2: Receive compressed tensor
buffer = b''
while True:
    chunk, _ = sock.recvfrom(4096)
    buffer += chunk
    if len(chunk) < 4096:
        break

# Step 3: Decompress
tensor = decompress_tensor(buffer, shape)
print("Received tensor with shape", tensor.shape)

# Step 4: Forward through remaining model
with torch.no_grad():
    remaining = model.model[-1][2:]  # Continue from 3rd conv layer
    output = tensor
    for layer in remaining:
        output = layer(output)

print("Final Output:", output.shape)
