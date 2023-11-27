import socket as sc


def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Получено: {data.decode('utf-8')}")
    client_socket.close()


def start_server():
    import threading
    server = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))
    server.listen(5)
    print("сервер запущен на 0.0.0.0:5555")

    while True:
        client, addr = server.accept()
        print(f"Получено от: {addr[0]}:{addr[1]}")

        client_handler = threading.Thread(target=handle_client, args=[client])
        client_handler.start()


def second_task_server():
    import pickle
    with sc.socket(sc.AF_INET, sc.SOCK_STREAM) as server_socket:
        server_socket.bind(("127.0.0.1", 5555))
        server_socket.listen()
        print("сервер запущен")

        conn, addr = server_socket.accept()
        with conn:
            received_data = conn.recv(1024)

    received_obj = pickle.loads(received_data)

    print(f"Объект 1: {received_obj.property1}")
    print(f"объект 2: {received_obj.property2}")

    result = received_obj.some_method()
    print(result)


if __name__ == "__main__":
    menu = int(input("""Выберите дейтсвие:
1. Первый номер
2. Второй номер
3. Третий номер\n"""))
    match menu:
        case 1:
            start_server()
        case 2:
            second_task()
        case 3:

            pass