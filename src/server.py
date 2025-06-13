import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('0.0.0.0', 1003))

received_chunks = {}

print("Waiting for image data...")

while True:
    data, addr = server.recvfrom(4096)
    seq = int.from_bytes(data[:4], byteorder='big', signed=True)

    if seq == -1:
        print("EOF received.")
        break

    received_chunks[seq] = data[4:]  # Strip the sequence header

# Write all chunks in order to a file
with open("output.jpg", "wb") as f:
    for i in sorted(received_chunks.keys()):
        f.write(received_chunks[i])

server.close()
print("Image reassembled and saved.")
