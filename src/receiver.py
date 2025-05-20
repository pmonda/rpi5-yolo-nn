import socket
from PIL import Image
import time

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 5001
BUFFER_SIZE = 4096
OUTPUT_FILE = "received_image.png"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        with open(OUTPUT_FILE, "wb") as f:
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                f.write(data)
        print(f"File saved as {OUTPUT_FILE}")

    # Optional: open image to verify
    time.sleep(0.1)
    try:
        img = Image.open(OUTPUT_FILE)
        img.show()
    except Exception as e:
        print(f"Could not open image: {e}")
