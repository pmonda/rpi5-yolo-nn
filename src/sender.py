import socket
import time

serverAddress = ("192.168.1.205", 2222)  # Replace with your PC's IP
bufferSize = 1024
UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

with open("pmh2mmc4.png", "rb") as f:
    data = f.read(bufferSize)
    while data:
        UDPClient.sendto(data, serverAddress)
        data = f.read(bufferSize)

# Send end marker
UDPClient.sendto("end image".encode('utf-8'), serverAddress)
print("Image sent.")