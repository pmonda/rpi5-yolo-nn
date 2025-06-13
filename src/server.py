import socket
import pickle

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('0.0.0.0', 1003))

print("Listening for image chunks...")
received = {}

while True:
    data, addr = server.recvfrom(4096)
    try:
        packet = pickle.loads(data)
    except Exception as e:
        print("Deserialization error:", e)
        continue

    if 'done' in packet:
        print(f"Done receiving. Total chunks: {packet['total_chunks']}")
        break

    seq = packet['seq']
    chunk = packet['data']
    received[seq] = chunk

# Write image
with open("output.jpg", "wb") as f:
    for i in sorted(received.keys()):
        f.write(received[i])

server.close()
print("Image reassembled and saved.")
