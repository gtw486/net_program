from socket import *
import os

BASE_DIR = os.path.join(os.getcwd(), 'HW5')

def get_mime_type(filename):
    if filename.endswith('.html'):
        return 'text/html', 'r', 'utf-8'
    elif filename.endswith('.png'):
        return 'image/png', 'rb', None
    elif filename.endswith('.ico'):
        return 'image/x-icon', 'rb', None
    else:
        return 'application/octet-stream', 'rb', None

s = socket()
s.bind(('', 80))
s.listen(10)

print('웹 서버 실행 중...')

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    if not data:
        c.close()
        continue

    msg = data.decode()
    req = msg.split('\r\n')
    request_line = req[0]
    print('요청:', request_line)

    try:
        method, path, version = request_line.split()
        filename = path.lstrip('/') or 'index.html'
        filepath = os.path.join(BASE_DIR, filename)
        print('찾는 파일 경로:', filepath)

        if not os.path.isfile(filepath):
            response = 'HTTP/1.1 404 Not Found\r\n\r\n<h1>404 Not Found</h1>'
            c.send(response.encode())
            c.close()
            continue

        mime_type, mode, encoding = get_mime_type(filename)

        if encoding:
            with open(filepath, mode, encoding=encoding) as f:
                body = f.read()
            header = f'HTTP/1.1 200 OK\r\nContent-Type: {mime_type}; charset={encoding}\r\n\r\n'
            c.send(header.encode() + body.encode(encoding))
        else:
            with open(filepath, mode) as f:
                body = f.read()
            header = f'HTTP/1.1 200 OK\r\nContent-Type: {mime_type}\r\n\r\n'
            c.send(header.encode() + body)

    except Exception as e:
        print(f"에러 발생: {e}")
        response = 'HTTP/1.1 500 Internal Server Error\r\n\r\n<h1>500 Server Error</h1>'
        c.send(response.encode())

    c.close()