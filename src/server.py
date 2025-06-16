# receiver.py
import socket
import pickle
import signal
import sys
import time

UDP_IP = "0.0.0.0"
UDP_PORT = 5005
TIMEOUT = 10
MAX_RETRIES = 3

def signal_handler(sig, frame):
    print("\nShutting down server...")
    sock.close()
    sys.exit(0)

# Set up signal handler for graceful shutdown
signal.signal(signal.SIGINT, signal_handler)

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    sock.settimeout(TIMEOUT)
    print(f"Server listening on {UDP_IP}:{UDP_PORT}")
    print("Press Ctrl+C to stop the server")

    while True:
        try:
            print("Waiting for data...")
            data, addr = sock.recvfrom(1024)
            total_packets = int(data.decode())
            print(f"Expecting {total_packets} packets...")
            
            # Send acknowledgment for metadata
            sock.sendto(b"ACK", addr)
            
            received_data = bytearray()
            received_packets = set()
            start_time = time.time()
            
            while len(received_packets) < total_packets:
                try:
                    # Receive packet with sequence number
                    packet_data, _ = sock.recvfrom(4096 + 4)  # Extra 4 bytes for seq num
                    seq_num = int.from_bytes(packet_data[:4], 'big')
                    packet = packet_data[4:]
                    
                    if seq_num not in received_packets:
                        received_packets.add(seq_num)
                        received_data.extend(packet)
                        
                        # Send acknowledgment
                        sock.sendto(seq_num.to_bytes(4, 'big'), addr)
                        
                        if len(received_packets) % 100 == 0:
                            print(f"Received {len(received_packets)}/{total_packets} packets")
                
                except socket.timeout:
                    print("Packet timeout, waiting for retransmission...")
                    continue
            
            print("Deserializing data...")
            tensor = pickle.loads(received_data)
            elapsed = time.time() - start_time
            print(f"Transfer complete in {elapsed:.2f} seconds")
            print(f"Tensor shape: {tensor.shape}")
            print(f"Tensor device: {tensor.device}")
            print(f"Tensor type: {tensor.dtype}")
            print(tensor)

        except socket.timeout:
            print("Timeout waiting for initial data")
            continue
        except Exception as e:
            print(f"Error processing data: {e}")
            continue

except Exception as e:
    print(f"Server error: {e}")
finally:
    sock.close()
