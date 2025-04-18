from socket import *
import random

# 소켓 설정
port = 3333
BUFF_SIZE = 1024
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

print("서버 시작, 메시지 수신 대기 중...")

while True:
    sock.settimeout(None)  # 블로킹 모드 (무한 대기)
    try:
        # 클라이언트로부터 메시지 수신
        data, addr = sock.recvfrom(BUFF_SIZE)
        msg = data.decode()
        print(f"수신: {msg} from {addr}")

        # 50% 확률로 ACK를 보내지 않음 (데이터 손실 시뮬레이션)
        if random.random() <= 0.5:
            print("ACK 전송 스킵 (손실 시뮬레이션)")
            continue
        else:
            # ACK 전송
            sock.sendto(b'ack', addr)
            # 메시지에서 재전송 횟수와 실제 메시지 분리
            re_tx_count, chat_msg = msg.split(' ', 1)
            print(f"<- {chat_msg} (재전송 횟수: {re_tx_count})")
    except Exception as e:
        print(f"오류 발생: {e}")
        continue