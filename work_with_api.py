import requests

def get_request(url):
    response = requests.get(url)
    data = response.json().items()
    if response.status_code == 200:
        if url != "https://catfact.ninja/fact":
            for key, value in data:
                if key == 'data':
                    for key1 in value:
                        print(key1)
        else:
            for key, value in data:
                print(f"Ключ: {key}, значение: {value}")
    else:
        print('error')
    return

menu = 0
while menu != 4:
    print("1. Один факт")
    print("2. Много фактов")
    print("3. Список хлеба")
    print("4. Выход и программы")
    menu = int(input("Выберети пункт: "))
    if menu == 1: get_request("https://catfact.ninja/fact")
    elif menu == 2: get_request("https://catfact.ninja/facts")
    elif menu == 3: get_request("https://catfact.ninja/breeds")
    elif menu == 4: print("bye")
    else: print("Такого действия нет")