import math
from type import typing_text
from calculator import calculator
from area_and_volume_calculator import calculator_area_and_volume
menu = 0
print("1. Первое задание")
print("2. Второе задание")
print("3. Третье задание")
print("4. Выход")
while menu != 4:
    menu = int(input("Введите какое задание вы хотите проверить"))
    match menu:
        case 1:
            typing_text()
        case 2:
            calculator()
        case 3:
            calculator_area_and_volume()
