"""
Задание из методички:

1.	Сохранить данные из предыдущего домашнего задания в файл .json или .csv.
2.	Создать MongoDB, записать данные туда (любое название базы, любое название коллекции).
    Выполнить команду для демонстрации содержимого коллекции. Прикрепить скриншот.
3.	Создать базу данных sqlite, загрузить туда данные из парсера с предыдущего урока. Загрузить файл .db
"""
import json
import sqlite3

with open('vacancies.json', 'r', encoding='utf-8') as f:
    f_content = f.read()
    data_dict = json.loads(f_content)
    data_list = data_dict['data']

con = sqlite3.connect('sqlite.db')
cursor = con.cursor()
cursor.execute('DROP TABLE if exists vacancies')

query = '''
CREATE TABLE vacancies(
                id integer PRIMARY KEY,
                title text,
                link text,
                recruiter text,
                location text,
                salary_min integer,
                salary_max integer,
                salary_currency integer,
                source text)    
'''

cursor.execute(query)
con.commit()