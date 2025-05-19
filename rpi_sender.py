import socket
import time

bufferSize = 1024
msgFromServer = "Hello Client"
serverPort = 2222
serverIP = "192.168.1.204"
bytesToSend = msgFromServer.encode('utf-8')
RPIsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
RPIsocket.bind((serverIP,serverPort))
print('Server is Listening ...')
message, address = RPIsocket.recvfrom(bufferSize)
message = message.decode('utf-8')
print(message)
print('Client Address ', address[0])
RPIsocket.sendto(bytesToSend, address)
