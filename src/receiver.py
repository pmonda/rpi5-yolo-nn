
import socket
from PIL import Image
import time

listen_ip = '0.0.0.0'  # Listen on all interfaces
listen_port = 5005
buffer_size = 1024
end_marker = b'__end__'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((listen_ip, listen_port))

with open("received_image.png", "wb") as f:
    print("Listening for image data...")
    while True:
        data, addr = sock.recvfrom(buffer_size)
        if data == end_marker:
            print("End of image received.")
            break
        f.write(data)

time.sleep(0.1)  # Give system time to flush I/O

try:
    img = Image.open("received_image.png")
    img.show()
except Exception as e:
    print(f"Failed to open image: {e}")