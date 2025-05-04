import re
import pandas as pd

# Define the log file name
log_file = "benchmarks.log"
output_csv = "inference_times_with_format.csv"

# Read the log file
with open(log_file, "r") as file:
    log_data = file.readlines()

# Extract model names, formats, and inference times
model_times = []
current_model = None

for line in log_data:
    # Detect when a new model benchmark starts
    
    # Extract format and inference time from table rows
    match_time = re.search(r'(\S+)\s+✅\s+\d+\.\d+\s+\d+\.\d+\s+(\d+\.\d+)\s+\d+\.\d+', line)
    if match_time:
        model_format = match_time.group(1)  # Extract format (e.g., PyTorch, TorchScript)
        inference_time = float(match_time.group(2))  # Extract inference time
        model_times.append((model_format, inference_time))

# Convert to DataFrame
df = pd.DataFrame(model_times, columns=["Format", "Inference Time (ms)"])

# Save to CSV
df.to_csv(output_csv, index=False)

print(f"Extraction complete! Data saved to {output_csv}")
