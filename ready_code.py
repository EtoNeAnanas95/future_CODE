import socket as sc
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Получено: {data.decode('utf-8')}")
    client_socket.close()

def start_server():
    server = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
    server.bind(("62.197.149.22", 1111))
    server.listen(5)
    print("сервер запущен на 62.197.149.22:1111")

    while True:
        client, addr = server.accept()
        print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")

        client_handler = threading.Thread(target=handle_client, args=[client])
        client_handler.start()

if __name__ == "__main__": #этот код выступает чекером запущен ли метод из этого в файла, как моудль в другой в файл
    #если запустить этот файл самостоятельно с помощью кнопки в IDE или в терминале pythom ready_code.py, то код реал запустится
    #а если мы в main напишем import ready_code бла бла бла, и будем юзать какието методы от сюда, то ничего не запустится. ду ю ноу?
    start_server()







import socket
import time

def send_message(message):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))
    client.send(message.encode('utf-8'))
    client.close()

if __name__ == "__main__":
    messages = ["Hello", "How are you?", "Goodbye"]

    for message in messages:
        send_message(message)
        time.sleep(1)
