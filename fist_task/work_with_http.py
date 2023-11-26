import requests
from bs4 import BeautifulSoup

def get_title_value(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        title_tag = soup.find('title')
        if title_tag:
            title_value = title_tag.text.strip()
            return title_value
