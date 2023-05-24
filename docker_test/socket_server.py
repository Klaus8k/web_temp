# import requests
import datetime
import socket

HOST = '0.0.0.0'
PORT = 5000

def read_file():
    with open('1/1.txt', 'r') as file:
        return file.read()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    conn, addr = sock.accept()

    with conn:
        while True:
            data = conn.recv(1024)

            if not data:
                break

            data_str = data.decode(encoding="utf-8")
            responce = f'Получено -- {data_str} Добавка из файла: {read_file()} Время:{datetime.datetime.now()}'
            conn.sendall(bytes(responce, encoding='utf-8'))
            print(responce)


    
