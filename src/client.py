import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.1.205', 1003)

with open("pmh2mmc4.png", "rb") as file:
    while True:
        chunk = file.read(65000)
        if not chunk:
            break
        client.sendto(chunk, server_address)

# Optionally send an empty packet to signal EOF
client.sendto(b'EOF', server_address)

client.close()
