"""
1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
сохранить JSON-вывод в файле *.json.
"""


import requests
import json

username = "AntonDubovitskii"

url = f"https://api.github.com/users/{username}/repos"

# Делаем запрос и сохраняем результат в виде json в переменную data
data = requests.get(url).json()

# Сохранение данных о моих репозиториях от api github в json файл
with open('my_repos.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# Просто вывод в консоль названий всех моих репозиториев
for repo in data:
    print(repo['name'])