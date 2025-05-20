import socket
import time
from PIL import Image
bufferSize = 1024
msgFromServer = "Hello Client"
serverPort = 2222
serverIP = "192.168.1.204"
# bytesToSend = msgFromServer.encode('utf-8')
RPIsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RPIsocket.bind((serverIP,serverPort))
addr = (serverIP, serverPort)
print('Server is Listening ...')
# cnt = 0
while True:
    bytes = 0
    f = open("pmh2mmc4.png", "wb")
    data, addr = RPIsocket.recvfrom(bufferSize)
    while(data):
        f.write(data)
        RPIsocket.settimeout(20)
        bytes += len(data)
        data, adddr = RPIsocket.recvfrom(bufferSize)
        if data == "end image":
            f.close()
            Image.open("pmh2mmc4.png").show()
            time.sleep(20)
            break
    
    # message, address = RPIsocket.recvfrom(bufferSize)
    # message = message.decode('utf-8')
    # print(f"Port {address[1]}@{address[0]} says: {message}")

    # if message == 'INC':
    #     cnt += 1
    # if message == 'DEC':
    #     cnt -= 1
    
    # msg_orig = input("Send Message: ")
    # msg = msg_orig.encode('utf-8')
    # RPIsocket.sendto(msg, address)
    # if "bye" in msg_orig.lower():
    #     print("Client says bye, exiting...")
    #     RPIsocket.close()
    #     break
    
    
