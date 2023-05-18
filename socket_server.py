# import requests
import socket

HOST = '79.133.181.123'
PORT = 8000 



# выход по ctrl C
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen()
        conn, addr = sock.accept()

        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
                print(f'connect by {addr} -- {data.decode(encoding="utf-8")}')

    break

