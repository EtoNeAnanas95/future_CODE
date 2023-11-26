import socket as sc


def second_task():
    from my_module import MyClass
    import pickle
    obj_to_send = MyClass(property1=input("введите значение 1:\n"), property2=input("введите значение 2:\n"))
    serialized_obj = pickle.dumps(obj_to_send)
    with sc.socket(sc.AF_INET, sc.SOCK_STREAM) as client_socket:
        client_socket.connect(("127.0.0.1", 5555))
        client_socket.sendall(serialized_obj)


def first_task():
    import time
    import random
    while True:
        messages = ["bla", "bla bla", "ultra bla bla"]
        random.shuffle(messages)
        message = messages[0].encode("utf-8")
        send_massage(message)


def send_massage(message):
    client = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
    client.connect(("127.0.0.1", 5555))
    client.send(message)
    client.close()