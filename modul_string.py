def find_symbol() -> int:
    string = input("Ведите текст\n")
    char = chr(input("Ведите cимвол который хотите искать\n"))
    return string.find(char)


def get_uppercase_letters() -> int:
    string = input("Ведите текст \n")
    return [char for char in string if char.isupper()]


def get_lowercase_letters() -> int:
    string = input("Ведите текст \n")
    return [char for char in string if char.islower()]

def get_numerical_characters() -> int:
    string = input("Ведите текст \n")
    return [char for char in string if char.isdigit()]

def is_uppercase() -> int:
    char = input("Ведите cимвол\n")
    return char.isupper()

def is_lowercase() -> int:
    char = input("Ведите cимвол\n")
    return char.islower()

def is_digit() -> int:
    char = input("Ведите cимвол\n")
    return char.isdigit()

def count_substrings() -> int:
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
    return count
