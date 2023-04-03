"""
2. Изучить список открытых API (https://www.programmableweb.com/category/all/apis).
Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию.
Ответ сервера записать в файл.
"""
from pprint import pprint

import requests
import json

# Использовался сервис https://www.weatherapi.com/, пройдена регистрация, получен API Key
api_key = "25fc0057e37a4d31b4b91009230304"
city = "Moscow"
air_quality_data = "no"

url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi={air_quality_data}"

# Делаем запрос и сохраняем результат в виде json в переменную data
data = requests.get(url).json()

# Сохранение ответа от weatherapi в json файл
with open('weather.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

pprint(data)
