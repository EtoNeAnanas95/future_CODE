import math

def calculate_discriminant() -> None:
    a = float(input("Введите первый член квадратного уравнения\n"))
    b = float(input("Введите второй член квадратного уравнения\n"))
    c = float(input("Введите третий член квадратного уравнения\n"))
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"X первое: {x1}")
        print(f"X второк: {x2}\n\n")
    elif discriminant == 0:
        x = -b / (2*a)
        print(f"X: {x}\n")
    else: print("Корней нет\n\n")

def calculate_probability() -> None:

    m1 = int(input("Введите число благоприятных событий\n"))
    n1 = int(input("Введите число всех возможных событий\n"))

    P_of_A = m1/n1
    print(f"Вероятность первого события: {P_of_A}")

    m2 = int(input("Введите число благоприятных \n"))
    n2 = int(input("Введите число всех возможных событий\n"))

    P_of_B = m2/n2
    print(f"Вероятность второго события: {P_of_B}\n")

    menu = int(input("""Выберите дейсвтие: 
    1. Вероятность несовместных событий
    2. Вероятность совместных событий
    """))

#Я не понял как пользоваться формулами которые вы приложили, потому что не понятно как считать P(AB)
#Поэтому я взял формулы из инета

    match menu:
        case 1:
            veroyatnost_nesovmestnih_cobitii = P_of_A - P_of_B
            print(f"Вероятность несовместных событий будет равна: {veroyatnost_nesovmestnih_cobitii}\n\n")
        case 2:
            veroyatnost_sovmestnih_cobitii = P_of_A * P_of_B
            print(f"Вероятность несовместных событий будет равна: {veroyatnost_sovmestnih_cobitii}\n\n")
