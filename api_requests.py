import requests
def get_holidays(country_code):
    api_url = f"https://date.nager.at/api/v3/publicholidays/2023/{country_code}"
    response = requests.get(api_url)
    data = response.json()
    if response.status_code == 200:
        if data:
            return data
menu = ''
while menu != 'exit':
    print('Введите код страны\nДля выхода введите exit')
    menu = input()
    if menu != 'exit':
        holidays_data = get_holidays(menu)
        for item in holidays_data:
            print(f'Дата: {item["date"]} - название: {item["name"]}')
            print(f'Местное название: {item["localName"]}')
    else:
        break