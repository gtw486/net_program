import struct
import binascii

# Udphdr 클래스 정의
class Udphdr:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port      # 송신자 포트번호 (2바이트)
        self.dst_port = dst_port      # 수신자 포트번호 (2바이트)
        self.length = length          # 패킷 길이 (2바이트)
        self.checksum = checksum      # 체크섬 (2바이트)

    def pack_Udphdr(self):
        # !: 네트워크 바이트 순서, H: 2바이트 unsigned short
        packed = struct.pack('!HHHH', self.src_port, self.dst_port, self.length, self.checksum)
        return packed

# UDP 헤더 언패킹 함수
def unpack_Udphdr(buffer):
    # 8바이트 데이터를 4개의 2바이트 필드로 언패킹
    unpacked = struct.unpack('!HHHH', buffer[:8])
    return unpacked

# 각 필드 값을 반환하는 함수
def getSrcPort(unpacked):
    return unpacked[0]  # Source Port

def getDstPort(unpacked):
    return unpacked[1]  # Destination Port

def getLength(unpacked):
    return unpacked[2]  # Length

def getChecksum(unpacked):
    return unpacked[3]  # Checksum

# 테스트 코드
if __name__ == "__main__":
    # Udphdr 객체 생성
    udp = Udphdr(5555, 80, 1000, 0xFFFF)
    
    # UDP 헤더 패킹
    packed_udphdr = udp.pack_Udphdr()
    print("Packed UDP Header (Hex):", binascii.hexlify(packed_udphdr).decode())
    
    # UDP 헤더 언패킹
    unpacked_udphdr = unpack_Udphdr(packed_udphdr)
    print("Unpacked UDP Header:", unpacked_udphdr)
    
    # 각 필드 값 출력
    print(f"Source Port: {getSrcPort(unpacked_udphdr)}")
    print(f"Destination Port: {getDstPort(unpacked_udphdr)}")
    print(f"Length: {getLength(unpacked_udphdr)}")
    print(f"Checksum: {hex(getChecksum(unpacked_udphdr))}")