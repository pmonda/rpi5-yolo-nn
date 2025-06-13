import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.1.205', 1003)  # Replace with PC's IP

with open("pmh2mmc4.png", "rb") as file:
    seq = 0
    while True:
        chunk = file.read(4096 - 4)  # 4 bytes for sequence number
        if not chunk:
            break
        # Prepend sequence number (4 bytes, big-endian)
        packet = seq.to_bytes(4, byteorder='big') + chunk
        client.sendto(packet, server_address)
        seq += 1

# Send EOF packet with sequence number -1 (0xFFFFFFFF)
client.sendto((-1).to_bytes(4, byteorder='big', signed=True), server_address)

client.close()
print("Image sent.")
