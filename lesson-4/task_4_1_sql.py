"""
Задание из методички:

1.	Создать базу данных sqlite, загрузить туда данные из парсера с предыдущего урока. Загрузить файл .db
"""
import json
import sqlite3

# По заданию данные берем из json файла, сформированного в процессе выполнения дз3
with open('vacancies.json', 'r', encoding='utf-8') as f:
    f_content = f.read()
    data_dict = json.loads(f_content)
    data_list = data_dict['data']

con = sqlite3.connect('sqlite.db')
cursor = con.cursor()
cursor.execute('DROP TABLE if exists vacancies')

query_create_table = '''
CREATE TABLE vacancies(
                id integer PRIMARY KEY,
                title text,
                link text,
                recruiter text,
                location text,
                salary_min integer,
                salary_max integer,
                salary_currency text,
                source text)    
'''

cursor.execute(query_create_table)
con.commit()

query_insert_data = '''
INSERT INTO vacancies(
                id,
                title,
                link,
                recruiter,
                location,
                salary_min,
                salary_max,
                salary_currency,
                source)  
            VALUES(
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?)
'''

for number, item in enumerate(data_list):
    entity = (number+1, item['title'], item['link'], item['recruiter'], item['location'], item['salary_min'],
              item['salary_max'], item['salary_currency'], item['source'])
    cursor.execute(query_insert_data, entity)

con.commit()

