import socket
import random

HOST = 'localhost'
PORT = 9002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode()
            if message == 'Request':
                heartbeat = random.randint(40, 140)
                steps = random.randint(2000, 6000)
                cal = random.randint(1000, 4000)
                send_data = f"{heartbeat},{steps},{cal}"
                conn.sendall(send_data.encode())
            elif message == 'quit':
                break