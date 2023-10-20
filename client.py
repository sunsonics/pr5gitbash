import socket
import threading

# Функция для отправки сообщений
def send_message():
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

# Функция для получения сообщений
def receive_message():
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print("Сервер: " + message)

# Создаем клиентский сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Создаем потоки для отправки и получения сообщений
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)

# Запускаем потоки
send_thread.start()
receive_thread.start()
