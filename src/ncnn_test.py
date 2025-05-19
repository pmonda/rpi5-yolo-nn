from ultralytics import YOLO
import cv2
import numpy as np
import torch
import time

import ultralytics.engine.exporter as exporter

model = YOLO("yolo11n.pt")

all_formats = exporter.export_formats()["Argument"]
for format in all_formats:
    print(format)

for model_format in list(all_formats):
    model.benchmark(data="coco128.yaml", imgsz=640, format=model_format)
    



'''

This is what a benchmark would look along the lines of for a specified export model

image = cv2.imread("bus.jpg")  # Replace with your test image
image = cv2.resize(image, (640, 640))  # Ensure consistent input size
image = np.transpose(image, (2, 0, 1))  # Change HWC to CHW
image = np.expand_dims(image, axis=0)   # Add batch dimension (BCHW)
image = torch.from_numpy(image).float() / 255.0  # Normalize


# Measure inference time
num_runs = 10  # Run multiple times for stability
times = []

for _ in range(num_runs):
    start_time = time.time()
    results = model(image)
    end_time = time.time()
    
    times.append((end_time - start_time) * 1000)  # Convert to milliseconds

# Compute average inference time
avg_time = np.mean(times)
print(f"Average Inference Time: {avg_time:.2f} ms")

# Compute inference time per megapixel
image_size = 640 * 640 / 1e6  # Convert to megapixels
ms_per_mp = avg_time / image_size
print(f"Inference Time per Megapixel: {ms_per_mp:.2f} ms/Mpx")

'''
