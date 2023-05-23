FROM python:3.8

WORKDIR /app

COPY socket_server.py socket_server.py

EXPOSE 5000

ENV TZ Europe/Moscow

CMD ["python", "./socket_server.py"]
