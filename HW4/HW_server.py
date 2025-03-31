from socket import *

s =socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)

def calculate(expression):
    try:
        expression = expression.replace(" ", "")  
        
        if '+' in expression:
            num1, num2 = expression.split('+')
            result = int(num1) + int(num2)
        elif '-' in expression:
            num1, num2 = expression.split('-')
            result = int(num1) - int(num2)
        elif '*' in expression:
            num1, num2 = expression.split('*')
            result = int(num1) * int(num2)
        elif '/' in expression:
            num1, num2 = expression.split('/')
            result = round(int(num1) / int(num2), 1)
        else:
            return "ERROR"
        
        return str(result)

    except Exception as e:
        return "ERROR:"

print("hello")

while True:
    client, addr = s.accept()
    print(f"hello")

    while True:
        data = client.recv(1024).decode()
        if not data or data.lower() == 'q':
            break

        print(f"{data}")
        result = calculate(data)
        client.send(result.encode())

    client.close()
