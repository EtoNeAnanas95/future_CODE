def calculator() -> None:
    try:
        print("Выберите действие: ")
        print("""1. +
2. -
3. *
4. /
5. %
6. //
7. Степень""")
        menu = int(input())
        match menu:
            case 1:
                first_num = int(input("Введите первое число"))
                second_num = int(input("Введите второе число"))
                res = first_num + second_num
                print(res)
            case 2:
                first_num = int(input("Введите первое число"))
                second_num = int(input("Введите второе число"))
                res = second_num - first_num
                print(res)
            case 3:
                first_num = int(input("Введите первое число"))
                second_num = int(input("Введите второе число"))
                res = first_num * second_num
                print(res)
            case 4:
                first_num = int(input("Введите первое число"))
                second_num = int(input("Введите второе число"))
                res = first_num / second_num
                print(res)
            case 5:
                first_num = int(input("Введите первое число"))
                second_num = int(input("Введите второе число"))
                res = first_num % second_num
                print(res)
            case 6:
                first_num = int(input("Введите первое число"))
                second_num = int(input("Введите второе число"))
                res = first_num // second_num
                print(res)
            case 7:
                first_num = int(input("Введите первое число"))
                second_num = int(input("Введите второе число"))
                res = first_num ** second_num
                print(res)

    except ValueError:
        print("Вы ввели не верные данные")