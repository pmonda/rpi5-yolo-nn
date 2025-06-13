import socket
import pickle

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.1.50', 1003)  # Replace with PC's IP

with open("pmh2mmc4.png", "rb") as f:
    seq = 0
    while True:
        chunk = f.read(3000)  # Leave room for pickle overhead to stay < 4096
        if not chunk:
            break
        packet = {
            'seq': seq,
            'data': chunk
        }
        serialized = pickle.dumps(packet)
        client.sendto(serialized, server_address)
        seq += 1

# Send DONE signal
done_packet = pickle.dumps({'done': True, 'total_chunks': seq})
client.sendto(done_packet, server_address)
client.close()
print("Image sent.")
