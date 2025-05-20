import socket
import time

serverAddress = ('<PC_IP_ADDRESS>', 2222)  # Replace with your PC's IP
bufferSize = 1024

UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    with open("pmh2mmc4.png", "rb") as f:
        while True:
            data = f.read(bufferSize)
            if not data:
                break
            UDPClient.sendto(data, serverAddress)

    # Send end-of-image marker
    UDPClient.sendto(b"__end__", serverAddress)
    print("Image sent. Waiting before next transmission...")
    time.sleep(5)  # Delay between sends