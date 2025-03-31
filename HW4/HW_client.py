from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

print("start")
print("계산식: ")

while True:
    expression = input("입력: ")
    s.send(expression.encode())
    
    if expression.lower() == 'q':
        break
    
    result = s.recv(1024).decode()
    print(f"{result}")

s.close()