import socket
import select
import time

HOST = 'localhost'
PORT = 2500
BUFFER_SIZE = 1024

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind((HOST, PORT))
server_sock.listen()

print('Server Started on port', PORT)

sockets_list = [server_sock]
client_addresses = {}  # 클라이언트 소켓 : 주소

while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_sock:
            client_socket, client_addr = server_sock.accept()
            sockets_list.append(client_socket)
            client_addresses[client_socket] = client_addr
            print('new client', client_addr)
        else:
            try:
                data = notified_socket.recv(BUFFER_SIZE)
                if not data:
                    raise Exception("Disconnected")

                decoded = data.decode().strip()
                client_addr = client_addresses[notified_socket]

                # quit 입력 처리
                if 'quit' in decoded.lower():
                    print(client_addr, 'exited')
                    sockets_list.remove(notified_socket)
                    del client_addresses[notified_socket]
                    notified_socket.close()
                    continue

                # UDP 스타일 출력
                print(time.asctime() + str(client_addr) + ':' + decoded)

                # 다른 클라이언트에게 메시지 전송
                for client_socket in sockets_list:
                    if client_socket != server_sock and client_socket != notified_socket:
                        client_socket.send(data)

            except:
                client_addr = client_addresses.get(notified_socket, '(unknown)')
                print(client_addr, 'exited')
                sockets_list.remove(notified_socket)
                if notified_socket in client_addresses:
                    del client_addresses[notified_socket]
                notified_socket.close()

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        if notified_socket in client_addresses:
            del client_addresses[notified_socket]
        notified_socket.close()