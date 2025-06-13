import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.1.205', 1003)  # Replace with your PC's IP

with open("pmh2mmc4.png", "rb") as file:
    seq = 0
    while True:
        chunk = file.read(4090)  # 4090 bytes of image + 6 bytes of header
        if not chunk:
            break
        # Add 6-byte header: 2 bytes marker + 4 bytes sequence number
        header = b'PK' + seq.to_bytes(4, 'big')  # 'PK' is a fixed marker
        packet = header + chunk
        client.sendto(packet, server_address)
        seq += 1

# Send final DONE packet
client.sendto(b'DONE', server_address)
client.close()
print("Image sent.")
