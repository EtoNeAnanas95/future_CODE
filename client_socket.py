import socket as sc
import time
import random

def send_message():

    while True:
        messages = ["bla", "bla bla", "ultra bla bla"]
        random.shuffle(messages)
        message = messages[0].encode("utf-8")
        client = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
        client.connect(("127.0.0.1", 5555))
        client.send(message)
        client.close()
        time.sleep(10)

send_message()

