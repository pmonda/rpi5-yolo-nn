import torch
import zlib
import numpy as np
import socket
from ultralytics import YOLO

# Hooks dictionary
intermediate_outputs = {}

def save_output(name):
    def hook(module, input, output):
        # Save the output tensor from the hook
        intermediate_outputs[name] = output
    return hook

def attach_hooks(model):
    # Detection head layers: Adjust indexes as needed
    # Iterate over model layers and attach hooks
    layers = list(model.model.children())[:16]  # Adjust the slice as needed
    for i, layer in enumerate(layers):
        # Attach the hook to each layer individually
        layer.register_forward_hook(save_output(f"layer_{i}"))
    return model

def compress_tensor(tensor):
    """
    Compress the tensor using zlib and return the compressed data and its shape.
    """
    array = tensor.detach().cpu().numpy().astype(np.float32)
    shape = array.shape
    data = zlib.compress(array.tobytes())
    return data, shape

def decompress_tensor(data, shape):
    """
    Decompress the data and return a tensor with the given shape.
    """
    array = np.frombuffer(zlib.decompress(data), dtype=np.float32).reshape(shape)
    return torch.tensor(array)

# Example usage:

# Initialize the YOLO model
model = YOLO("yolo11n.pt")

# Attach hooks to the model
model = attach_hooks(model)

# Example input tensor (you can replace this with your actual input)
input_tensor = torch.rand((1, 3, 640, 640))  # Example tensor for YOLO input

# Perform a forward pass to trigger the hooks and store outputs
output = model(input_tensor)

# Access intermediate outputs after the forward pass
for name, output_tensor in intermediate_outputs.items():
    print(f"Output from {name}: {output_tensor.shape}")

# Example of compression and decompression
compressed_data, shape = compress_tensor(intermediate_outputs['layer_0'])
print(f"Compressed data shape: {shape}")

# Decompress the tensor data back
decompressed_tensor = decompress_tensor(compressed_data, shape)
print(f"Decompressed tensor shape: {decompressed_tensor.shape}")
