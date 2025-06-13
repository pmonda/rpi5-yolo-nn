import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('0.0.0.0', 1003))

with open("output.jpg", "wb") as file:
    while True:
        data, addr = server.recvfrom(4096)
        if data == b'EOF':  # end-of-file signal
            break
        file.write(data)

server.close()
