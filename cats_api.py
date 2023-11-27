import requests
from PIL import Image
from io import BytesIO

def get_cat_image(tag = None):
    base_url = "https://cataas.com/cat"
    if tag:
        url = f"{base_url}/{tag}"
    else:
        url = base_url
    response = requests.get(url)
    if response.status_code == 200:
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        image.show()
    else:
        print('error')

menu = 0
while menu != 3:
    print("1. Обычный кот\n2. Кот с параметром\n3. Выход")
    menu = int(input("Что выберишь?: "))
    if menu == 1: get_cat_image()
    elif menu == 2: get_cat_image(input("Введите параметр котика: "))
    else: print("Такой команды нет")
    print("Что-то пошло нетак")
