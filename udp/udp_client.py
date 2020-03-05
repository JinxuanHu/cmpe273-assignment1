import socket
from socket import timeout

UDP_IP = '127.0.0.1'
UDP_PORT = 4001
BUFFER_SIZE = 1024
MESSAGE = "ping"
SEPERATOR = "|"


def get_client_id():
    id = input("Enter client id:")
    return id

def send(id = 0):
    sequence = 0
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Connected to the server")
        print("Starting a file upload...")
        with open ("upload.txt","r") as file:
            line = file.readline()
            while line :
                while True:
                    s.sendto((str(sequence) + SEPERATOR + str(line)).encode(),(UDP_IP,UDP_PORT))
                    try:
                        data,ip = s.recvfrom(BUFFER_SIZE)
                    except timeout:
                        continue
                    data = data.decode().split(SEPERATOR)
                    ack = data[0]
                    if(int(ack) == sequence):
                        print(f"received ACK({ack})from the server{ip}.")
                        break
                sequence += 1
                line = file.readline()            
        print("File upload successfully completed.")
        file.close()
    except socket.error:
        print("Error! {}".format(socket.error))
        exit()
    
if __name__ == "__main__":
    send(get_client_id)

         
