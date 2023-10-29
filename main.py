from defs import calculate_days_lived, investment, count_substring, summator
from calculator import calculate_discriminant, calculate_probability
from module_string import *
from exception import transfer_money, MoneyError
from convert import convert
from os import system as command
from msvcrt import getch

try:
    while True:
        command("cls")
        menu = int(input("""Выберите дейсвтия:
    1. Калькулятор возраста
    2. Калькулятор инвестиций
    3. Калькулятор подстрок
    4. Сумматор
    5. Модуль арифметики
    6. Модуль строк
    7. Безопасная конвертация типов
    8. Перевод денег
    9. Выход
    """))
        match menu:
            case 1:
                calculate_days_lived()
            case 2:
                investment()
            case 3:
                count_substring()
            case 4:
                summator()
            case 5:
                command("cls")
                menu = int(input("""Выберите дейсвтия:
    1. Калькулятор квадратных уравнений
    2. Калькулятор вероятностей
    """))
                match menu:
                    case 1:
                        calculate_discriminant()
                    case 2:
                        calculate_probability()
            case 6:
                command("cls")
                menu = int(input("""Выберите дейсвтия:
    1. - Поиск символа в прописанной строке
    2. - Возврат списка заглавных букв
    3. - Возврат списка строчных букв
    4. - Возврат списка числовых символов
    5. - Проверка символа на принадлежность к заглавным буквам
    6. - Проверка символа на принадлежность к строчным буквам
    7. - Проверка символа на принадлежность к цифрам
    8. - Подсчет подстрок в указанной строке;
    """))
                match menu:
                    case 1:
                        print(find_symbol())
                        print('Нажмите любую клавишу, чтобы продолжить', end='', flush=True)
                        getch()
                    case 2:
                        print(get_uppercase_letters())
                        print('Нажмите любую клавишу, чтобы продолжить', end='', flush=True)
                        getch()
                    case 3:
                        print(get_lowercase_letters())
                        print('Нажмите любую клавишу, чтобы продолжить', end='', flush=True)
                        getch()
                    case 4:
                        print(get_numerical_characters())
                        print('Нажмите любую клавишу, чтобы продолжить', end='', flush=True)
                        getch()
                    case 5:
                        print(is_uppercase())
                        print('Нажмите любую клавишу, чтобы продолжить', end='', flush=True)
                        getch()
                    case 6:
                        print(is_lowercase())
                        print('Нажмите любую клавишу, чтобы продолжить', end='', flush=True)
                        getch()
                    case 7:
                        print(is_digit())
                        print('Нажмите любую клавишу, чтобы продолжить', end='', flush=True)
                        getch()
                    case 8:
                        print(count_substrings())
                        print('Нажмите любую клавишу, чтобы продолжить', end='', flush=True)
                        getch()
            
            case 7:
                value = input("Введите значение переменной для конвертации: ")
                types = {
                    "int": int,
                    "float": float,
                    "str": str,
                    "list": list,
                    "bool": bool
                }

                choosen_type = input("Введите тип в который будет конвертирована переменная: ")

                if choosen_type not in types: 
                    break

                _type = types[choosen_type]

                print(f"Тип до конвертации: {type(value).__name__}")
                value = convert(value, _type)
                print(f"Тип после конвертации: {type(value).__name__}")

                getch()

            case 8:
                try:
                    sender = str(input("Введите имя отправителя: "))
                    recipient = str(input("Введите имя получателя: "))
                    amount = int(input("Введите кол-во денег: "))
                    transfer_money(sender, recipient, amount)
                    print(f"Деньги были переведены от {sender} к {recipient} ")
                except MoneyError as e:
                    print(f"Не удалось перевести деньги. Ошибка: {e}")

                getch()

            case 9:
                quit()
except ValueError: print("Данные введен не верно\n\n")