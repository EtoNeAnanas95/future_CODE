from defs import calculate_days_lived, investment, count_substring, summator
from caculator import calculate_discriminant, calculate_probability
from modul_string import *
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
    7. Выход
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
                quit()
except ValueError: print("Данные введен не верно\n\n")