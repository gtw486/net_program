from socket import *
BUFF_SIZE = 1024
port = 5555
c_sock = socket(AF_INET, SOCK_DGRAM)
c_sock.connect(('localhost', port))
for i in range(10): # 10번 전송
    time = 0.1 # 0.1초
    data = 'Hello, IoT'
    while True:
        c_sock.send(data.encode())
        print('Packet({}): Waiting up to {} secs for ack'.format(i, time))
        c_sock.settimeout(time)
        try:
            data = c_sock.recv(BUFF_SIZE)
        except timeout:
            time *= 2 # 대기시간 2배 증가
            if time > 2.0: # 최대 대기시간 초과
                break
        else:
            print('Response', data.decode())
            break