import socket
import threading

HOST = 'localhost'
PORT = 2500

def recv_handler(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())
        except:
            break

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

my_id = input("ID를 입력하세요: ")
sock.send(f"[{my_id}]".encode())

recv_thread = threading.Thread(target=recv_handler, args=(sock,))
recv_thread.daemon = True
recv_thread.start()

while True:
    msg = input()
    full_msg = f"[{my_id}] {msg}"
    sock.send(full_msg.encode())

    if msg.lower() == 'quit':
        sock.close()
        break