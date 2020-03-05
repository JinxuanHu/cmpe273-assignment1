import socket
import threading

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024

def tcp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(10)
    print("Server started at port " + str(TCP_PORT))

    while True:
        conn, addr = s.accept()
        print(f'Connection address:{addr}')
        try:
            add_thread = threading.Thread(target = client_thread, args = (conn, addr))
            add_thread.start()
        except:
            print("failed")
    conn.close()

def client_thread(conn, addr):
    true = True
    while true:
        data = conn.recv(BUFFER_SIZE).decode()
        if not data :   
            # print('No data received.')
            true = False
            break
        print(f"received data:{data}")
        conn.send("pong".encode())

if __name__ == "__main__":
    tcp_server()