# import requests
import datetime
import socket

HOST = '0.0.0.0'
PORT = 5000



count = 0

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen()
        conn, addr = sock.accept()

        with conn:
            while count < 3:

                with open('1/1.txt', 'r') as file:
	                adder = file.read()

                data = conn.recv(1024)

                if not data:
                    break
                data_str = data.decode(encoding="utf-8")
                responce = f'Получено -- {data_str} Добавка из файла: {adder} Время:{datetime.datetime.now()}'
                conn.sendall(bytes(responce, encoding='utf-8'))
                print(responce)
                count += 1
    
