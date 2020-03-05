import socket
import threading
import sys
import time


TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
MESSAGE = "ping"

def get_client_id():
    id = sys.argv[1]
    return id

delay = int(sys.argv[2])
nums = int(sys.argv[3])

def tcp_client(id):
    count = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    while count < nums:
        s.send(f"{id}:{MESSAGE}".encode())
        print(f"Sending data: {MESSAGE}")
        data = s.recv(BUFFER_SIZE)
        print("received data:", data.decode())
        count += 1
        time.sleep(delay)
    s.close()

if __name__ == "__main__":
    tcp_client(get_client_id())