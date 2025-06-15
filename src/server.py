# receiver.py
import socket
import pickle

UDP_IP = "0.0.0.0"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

# Receive metadata
data, addr = sock.recvfrom(1024)
total_packets = int(data.decode())

# Receive all chunks
received_data = bytearray()
for _ in range(total_packets):
    packet, _ = sock.recvfrom(4096)
    received_data.extend(packet)

# Deserialize
tensor = pickle.loads(received_data)
print(tensor.shape)
