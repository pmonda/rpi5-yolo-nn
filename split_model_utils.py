import torch
import zlib
import numpy as np
import socket
from ultralytics import YOLO

# Hooks dictionary
intermediate_outputs = {}

def save_output(name):
    def hook(module, input, output):
        intermediate_outputs[name] = output
    return hook

def attach_hooks(model):
    # Detection head layers: Adjust indexes as needed
    model.model[-1][0].register_forward_hook(save_output("conv1"))
    model.model[-1][1].register_forward_hook(save_output("conv2"))
    return model

def compress_tensor(tensor):
    array = tensor.detach().cpu().numpy().astype(np.float32)
    shape = array.shape
    data = zlib.compress(array.tobytes())
    return data, shape

def decompress_tensor(data, shape):
    array = np.frombuffer(zlib.decompress(data), dtype=np.float32).reshape(shape)
    return torch.tensor(array)
