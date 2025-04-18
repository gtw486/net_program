from socket import *
import time

# 소켓 설정
server_addr = ('127.0.0.1', 3333)  
BUFF_SIZE = 1024
sock = socket(AF_INET, SOCK_DGRAM)

print("클라이언트 시작, 메시지를 입력하세요.")

while True:
    msg = input('-> ')
    if not msg:  
        break

    reTx = 0
    while reTx <= 5:
        resp = f"{reTx} {msg}"
        print(f"전송: {resp}")
        sock.sendto(resp.encode(), server_addr)

        # 2초 타임아웃 설정
        sock.settimeout(2)
        try:
            # ACK 수신 대기
            data, addr = sock.recvfrom(BUFF_SIZE)
            if data.decode() == 'ack':
                print("ACK 수신, 전송 성공")
                break
        except timeout:
            print(f"타임아웃 발생, 재전송 시도 ({reTx + 1}/5)")
            reTx += 1
            if reTx > 5:
                print("최대 재전송 횟수 초과, 전송 실패")
                break
            continue

sock.close()