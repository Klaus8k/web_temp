# import requests
import socket
import datetime

HOST = '0.0.0.0'
PORT = 5000

with open('./files_for_docker/1.txt', 'r') as file:
	x = file.read()

count = 0
while count < 3:
	count += 1
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
                print(f'connect by {addr} -- {data.decode(encoding="utf-8")} --{x}-- {datetime.datetime.now()}')

    break

