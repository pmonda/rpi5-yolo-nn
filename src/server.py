import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('0.0.0.0', 1003))  # Listen on all interfaces

print("Waiting for image data...")
received = {}

while True:
    data, addr = server.recvfrom(4096)
    if data == b'DONE':
        break

    if data[:2] == b'PK':  # Our packet marker
        seq = int.from_bytes(data[2:6], 'big')
        chunk = data[6:]
        received[seq] = chunk

# Reassemble in correct order
with open("output.jpg", "wb") as file:
    for i in sorted(received.keys()):
        file.write(received[i])

server.close()
print("Image received.")
