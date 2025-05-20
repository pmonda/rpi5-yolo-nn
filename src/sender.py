
import socket

# Replace with your PC's IP address
receiver_ip = '192.168.1.100'
receiver_port = 5005
buffer_size = 1024
end_marker = b'__end__'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = (receiver_ip, receiver_port)

with open("image.png", "rb") as f:
    while True:
        chunk = f.read(buffer_size)
        if not chunk:
            break
        sock.sendto(chunk, address)

# Send end-of-image marker
sock.sendto(end_marker, address)
print("Image sent.")