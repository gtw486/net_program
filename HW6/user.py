import socket
import time

# 디바이스 IP와 포트 설정
DEVICE1_ADDR = ('localhost', 9001)  # 디바이스 1
DEVICE2_ADDR = ('localhost', 9002)  # 디바이스 2

# 디바이스 연결
device1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
device1.connect(DEVICE1_ADDR)

device2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
device2.connect(DEVICE2_ADDR)

print("디바이스 1, 2 연결 완료")

# 파일 열기 (없으면 생성됨)
file_name = 'data.txt'

while True:
    user_input = input("'1'/'2'/ 'quit'(종료) 입력: ")

    if user_input == '1':
        device1.sendall(b'Request')
        data = device1.recv(1024).decode()
        now = time.ctime()
        log = f"{now}: Device1: {data}\n"
        print(log.strip())
        with open(file_name, 'a') as f:
            f.write(log)

    elif user_input == '2':
        device2.sendall(b'Request')
        data = device2.recv(1024).decode()
        now = time.ctime()
        log = f"{now}: Device2: {data}\n"
        print(log.strip())
        with open(file_name, 'a') as f:
            f.write(log)

    elif user_input == 'quit':
        device1.sendall(b'quit')
        device2.sendall(b'quit')
        device1.close()
        device2.close()
        print("종료")
        break

    else:
        print("잘못 입력했어. 다시 입력해줘")