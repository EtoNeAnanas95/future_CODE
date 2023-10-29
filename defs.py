import datetime


def calculate_days_lived() -> None:
    year_of_Birth = int(input("Впишите год рождения\n"))
    month_of_Birth = int(input("Впишите месяц рождения\n"))
    day_of_Birth = int(input("Впишите день рождения\n"))
    current_date = datetime.date.today()
    birth_date = datetime.date(year_of_Birth, month_of_Birth, day_of_Birth)
    delta = current_date - birth_date
    print(f"Количество прожитых дней: {delta} \n\n")


def investment() -> None:
    initial_amount = int(input("Введите начальную сумму\n"))
    annual_interest_rate = int(input("Введите годовау процентнаю ставку\n"))
    number_of_interest_periods_per_year = int(input("Введите количество периодов начисления процентов в год\n(напр. при ежемесячном начислении процентов количество таких периодов будет 12)\n"))
    investment_period_in_years = int(input("Введите срок инвестиций в годах\n"))

    total_sum = ((1+annual_interest_rate/number_of_interest_periods_per_year)**(number_of_interest_periods_per_year*investment_period_in_years))*initial_amount
    print(f"Вы скопите: {total_sum} рублей\n\n")


def count_substring() -> None:
    substring = input("Введите сабстроку\n")
    text = input("Введите текст в котором будет искаться сабстрока\n")
    count = 0
    start = 0

    while start < len(text):
        pos = text.find(substring, start)
        if pos == -1:
            break
        else:
            count += 1
            start = pos + 1
    print(f"{count}\n\n")


def summator() -> None:
        total_sum = 0
        nums = []
        print("Для выхода нажмите ESCAPE")

        while True:
            print("""Выберите действие:
1. Добавить число
2. Выход
""")
            menu = int(input())
            match menu:
                case 1:
                    num = float(input("Ввыедите число\n"))
                    nums.append(num)
                case 2:
                    break
        for num in nums:
            if isinstance(num, (int, float)):
                total_sum += num
        print(f"Сумма всех цифр: {total_sum}\n\n")
