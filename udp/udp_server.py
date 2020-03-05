import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
MESSAGE = "pong"
SEPERATOR = "|"

def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", UDP_PORT))
    print("Server started at port." + str(UDP_PORT))
    print("Accepting a file upload...")

    while True:
        data, ip = s.recvfrom(BUFFER_SIZE)
        data_decoded = data.decode().split(SEPERATOR)
        # print("|||||||")
        # print(data_decoded)
        ack = data_decoded[0]
        msg = data_decoded[1]
        # print("##################")
        # print(ip)
        # print(msg)
        print("Recieving Data from client " + str(ip) + ":" + str(msg))
        s.sendto((ack + SEPERATOR + MESSAGE).encode(), ip)
    print("Upload successfully completed.")

if __name__ == "__main__":
    listen_forever()