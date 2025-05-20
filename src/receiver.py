import socket
from PIL import Image
import time

bufferSize = 1024
serverIP = "0.0.0.0"  # Listen on all interfaces
serverPort = 2222

RPIsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RPIsocket.bind((serverIP, serverPort))

print('Receiver is Listening ...')

while True:
    with open("received_image.png", "wb") as f:
        while True:
            data, addr = RPIsocket.recvfrom(bufferSize)
            if data == b"__end__":
                break
            f.write(data)

    try:
        img = Image.open("received_image.png")
        img.show()
        print("Image received and displayed.")
    except Exception as e:
        print(f"Error opening image: {e}")

    time.sleep(5)  # Optional wait between receptions