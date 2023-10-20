import socket
import threading

# Создаем серверный сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))
server_socket.listen(5)
print("Сервер запущен. Ожидание подключений...")

# Список клиентских соксов
client_sockets = []

# Функция для обработки сообщений от клиентов
def handle_client(client_socket):
    while True:
        try:
            # Получаем сообщение от клиента
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            print(f"Получено сообщение: {message}")

            # Рассылаем сообщение всем клиентам, кроме отправителя
            for client in client_sockets:
                if client != client_socket:
                    try:
                        client.send(message.encode('utf-8'))
                    except:
                        # Удалить оборванные соединения
                        client_sockets.remove(client)
        except:
            # Удалить оборванные соединения
            client_sockets.remove(client_socket)

    # Закрываем соединение и удаляем клиентский сокс
    client_socket.close()
    client_sockets.remove(client_socket)

# Основной цикл сервера
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Получено подключение от {client_address[0]}:{client_address[1]}")
    client_sockets.append(client_socket)
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
