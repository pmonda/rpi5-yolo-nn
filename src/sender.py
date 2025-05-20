import socket

SERVER_IP = '192.168.1.205'  # Change to your PC IP address
SERVER_PORT = 5001
BUFFER_SIZE = 4096
FILE_PATH = "pmh2mmc4.png"  # Change to your image file

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((SERVER_IP, SERVER_PORT))
    print(f"Connected to server {SERVER_IP}:{SERVER_PORT}")

    with open(FILE_PATH, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            sock.sendall(bytes_read)

    print("Image sent successfully.")
