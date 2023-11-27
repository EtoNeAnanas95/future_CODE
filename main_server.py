from client_socket import *
from server_socket import *
from work_with_http import *


menu = int(input("""Выберите дейтсвие:
   1. Первый номер
   2. Второй номер
   3. Третий номер
   4. Четвёртый номер\n"""))
match menu:
    case 1:
        start_server()
    case 2:
        second_task_server()
    case 3:
        menu_second = int(input("""Выберите сокет:
   1. Server
   2. Client\n"""))
        match menu_second:
            case 1:
                start_server()
            case 2:
                message = input("Введите сообщение:\n")
                send_massage(message)
    case 4:
        url = "http://example.org"
        print(f"по ссылке {url}, значение {get_title_value(url)}")