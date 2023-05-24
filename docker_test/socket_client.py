import socket
import sys

HOST = '79.133.181.123'
PORT = 8000
data = ' '.join(sys.argv[1:])


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data, encoding='utf-8'))
    responce = sock.recv(1024)

print(responce.decode(encoding='utf-8'))