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
    server.bind(("0.0.0.0", 5555))
    server.listen(5)
    print("сервер запущен на 0.0.0.0:5555")

    while True:
        client, addr = server.accept()
        print(f"Получено от: {addr[0]}:{addr[1]}")

        client_handler = threading.Thread(target=handle_client, args=[client])
        client_handler.start()

if __name__ == "__main__":
    start_server()