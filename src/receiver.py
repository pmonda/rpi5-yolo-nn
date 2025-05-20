import socket
import time
# msgFromClient = "Hello Server from Client"
# bytesToSend = msgFromClient.encode('utf-8')
serverAddress = ('192.168.1.204', 2222) #RPI address
bufferSize = 1024
UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    f = open("pmh2mmc4.png", "rb")
    data = f.read(bufferSize)
    while(data):
        if (UDPClient.sendto(data, serverAddress)):
            data = f.read(bufferSize)
    
    f.close()
    UDPClient.sendto("end image", serverAddress)
    time.sleep(0.2)
    # cmd = input("Send Message: ")
    # # cmd = input('What do you want to do with counter, INC or DEC? ')
    # cmd = cmd.encode('utf-8')
    # UDPClient.sendto(cmd, serverAddress)
    # data, address = UDPClient.recvfrom(bufferSize)
    # data = data.decode('utf-8')
    # print(f"Port {address[1]}@{address[0]} says: {data}")
    # if "bye" in data.lower():
    #     print("Server says bye, closing client")
    #     UDPClient.close()
    #     break
