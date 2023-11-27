import requests

def get_valorant(country_code):
    url = f"https://valorant-api.com/v1/{country_code}?language=ru-RU"
    try:
        response = requests.get(url)
        data = response.json()
        if data:
            if response.status_code == 200:
                return data
    except Exception as e:
        print(e)
menu = 0
while menu != 5:
    print("1. Агенты")
    print("2. Ивенты")
    print("3. Карты")
    print("4. Предметы")
    print("5. Выход")
    try:
        menu = int(input('Выберите: '))
        if menu == 1:
            agents_data = get_valorant("agents")
            for item in agents_data['data']:
                try:
                    print(f"Имя: {item['displayName']} - роль: {item['role']['displayName']}")
                except:
                    continue
        elif menu == 2:
            events_data = get_valorant("events")
            for item in events_data['data']:
                try:
                    print(f"Краткое название ивента: {item['shortDisplayName']} - начало: {item['startTime']}")
                except:
                    continue
        elif menu == 3:
            maps_data = get_valorant("maps")
            for item in maps_data['data']:
                try:
                    print(f"Название карты: {item['displayName']} - пленты: {item['tacticalDescription']}")
                except:
                    continue
        elif menu == 4:
            weapons_data = get_valorant("weapons")
            for item in weapons_data['data']:
                try:
                    print(f"Название: {item['displayName']}\nТип: {item['shopData']['categoryText']}")
                    print(f"Стоимость: {item['shopData']['cost']}\n{'-' * 18}")
                except:
                    continue
        elif menu == 5:
            break
    except:
        print("Введите корректное значение")
