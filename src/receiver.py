# receiver.py (on PC)
import socket
import time
from PIL import Image

bufferSize = 1024
serverPort = 2222
serverIP = "0.0.0.0"  # Listen on all interfaces

RPIsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RPIsocket.bind((serverIP, serverPort))

print("Receiver listening on port 2222...")
f = open("received_image.png", "wb")

while True:
    data, addr = RPIsocket.recvfrom(bufferSize)
    if data.decode(errors="ignore") == "end image":
        print("End of image transmission received.")
        break
    f.write(data)

f.close()
Image.open("received_image.png").show()
