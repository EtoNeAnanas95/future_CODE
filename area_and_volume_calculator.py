def calculator_area_and_volume() -> None:
    try:
        print("Выберите вид фигуры: ")
        print("1. Двухмерная")
        print("2. Трехмерная")
        figure = int(input())
        match figure:
            case 1:
                print("Выберите фигуру: ")
                print("1. Прямоугольник")
                print("2. Квадрат")
                print("3. Круг")
                print("4. Треугольник")
                print("5. Прямоугольный треугольник")
                figure_tip = int(input())
                match figure_tip:
                    case 1:
                        l = int(input("Введите длину"))
                        w = int(input("Введите ширину"))
                        S = l * w
                        print(F"Площадь прямоугольника равна: {S}")
                    case 2:
                        l = int(input("Введите длину любой стороны квадрата"))
                        S = l ** 2
                        print(F"Площадь квадрата равна: {S}")
                    case 3:
                        r = int(input("Введите радиус круга"))
                        p = 3,1415
                        S = r * p
                        print(F"Площадь круга равна: {S}")
                    case 4:
                        b = int(input("Введите длину основания треугольника"))
                        h = int(input("Введите высоту треугольника"))
                        S = 0,5 * b * h
                        print(F"Площадь треугольника равна: {S}")
                    case 5:
                        a = int(input("Введите длину первого катета"))
                        b = int(input("Введите длину второго катета"))
                        S = 0,5 * a * b
                        print(F"Площадь прямоугольного треугольника равна: {S}")

            case 2:
                print("Выберите фигуру: ")
                print("1. Прямоугольный параллелипипед")
                print("2. Куб")
                print("3. Шар")
                print("4. Конус")
                figure_tip = int(input())
                match figure_tip:
                    case 1:
                        print("Выберите что вы хотите посчитать")
                        print("1. Площадь")
                        print("2. Объём")
                        action = int(input())
                        match action:
                            case 1:
                                l = int(input("Введите длину первой стороны"))
                                w = int(input("Введите длину первой стороны"))
                                h = int(input("Введите длину первой стороны"))
                                S = 2 * l * w + 2 * l * h + 2 * w * h
                                print(F"Площадь прямоугольнго параллелипипеда равена: {S}")
                            case 2:
                                a = int(input("Введите длину первой стороны"))
                                b = int(input("Введите длину второй стороны"))
                                h = int(input("Введите высоту"))
                                V = a * b * h
                                print(F"Объём прямоугольнго параллелипипеда равен: {V}")
                    case 2:
                        print("Выберите что вы хотите посчитать")
                        print("1. Площадь")
                        print("2. Объём")
                        action = int(input())
                        match action:
                            case 1:
                                l = int(input("Введите длину"))
                                w = int(input("Введите ширину"))
                                h = int(input("Введите высоту"))
                                S = l * w * h
                                print(F"Площадь куба равна: {S}")
                            case 2:
                                l = int(input("Введите длину одной из сторон куьа"))
                                V = 6*l**2
                                print(f"Объём куба равен: {V}")
                    case 3:
                        print("Выберите что вы хотите посчитать")
                        print("1. Площадь")
                        print("2. Объём")
                        action = int(input())
                        match action:
                            case 1:
                                p = 3,1415
                                r = int(input("Введите радиус сферы"))
                                S = 4 * p * r ** 2
                                print(F"Площадь сферы равна: {S}")
                            case 2:
                                p = 3, 1415
                                r = int(input("Введите радиус сферы"))
                                V = 4 / 3 * p * r ** 3
                                print(f"Объём куба равен: {V}")
                    case 4:
                        print("Выберите что вы хотите посчитать")
                        print("1. Площадь")
                        print("2. Объём")
                        action = int(input())
                        match action:
                            case 1:
                                print("Площадь можно рссчитывать только для прямых конусов, БУДТЕ ВНИМАТЕЛЬНЫ!!!")
                                p = 3, 1415
                                r = int(input("Введите радиус конуса"))
                                S = p * r
                                SB = p * r ** 2
                                SA = S + SB
                                print(F"Площадь поверхности конуса равна: {S}")
                            case 2:
                                print("Объём можно рссчитывать только для прямых конусов, БУДТЕ ВНИМАТЕЛЬНЫ!!!")
                                p = 3, 1415
                                r = int(input("Введите радиус конуса"))
                                h = int(input("Введите высоту конуса"))
                                SB = p * r ** 2
                                V = (1/3) * SB * h
                                print(f"Объём куба равен: {V}")
    except ValueError:
        print("Вы ввели не верные данные")