"""
Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы)
с сайтов Superjob и HH. Приложение должно анализировать несколько страниц сайта
(также вводим через input или аргументы). Получившийся список должен содержать в себе минимум:

- Наименование вакансии.
- Предлагаемую зарплату (отдельно минимальную и максимальную).
- Ссылку на саму вакансию.
- Сайт, откуда собрана вакансия.

По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение).
Структура должна быть одинаковая для вакансий с обоих сайтов.
Общий результат можно вывести с помощью dataFrame через pandas.

Можно выполнить по желанию один любой вариант или оба при желании и возможности.
"""
import json
import requests
from bs4 import BeautifulSoup as bs

vacancy = input('Введите интересующую профессию: ').lower()  # Введено "Врач-терапевт"

data_list = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/111.0.0.0 Safari/537.36',
}

"""
Парсим hh.ru
"""
for number in range(1, 3):  # Парсятся первые 3 страницы
    url = f'https://spb.hh.ru/search/vacancy?text={vacancy}&area={number}'
    response = requests.get(url, headers=headers)
    soup = bs(response.text, 'html.parser')

    vac_item_list_hh = list(soup.find_all('div', {'class': 'vacancy-serp-item-body__main-info'}))

    for item in vac_item_list_hh:
        temp_dict = {}

        temp_dict['title'] = item.find('a', {'class': 'serp-item__title'}).text
        temp_dict['link'] = item.find('a', {'class': 'serp-item__title'})['href']
        temp_dict['recruiter'] = item.find('a', {'class': 'bloko-link bloko-link_kind-tertiary'})\
            .text.replace(u'\xa0', u' ')
        temp_dict['location'] = item.find('div', {'data-qa': 'vacancy-serp__vacancy-address'})\
            .text.replace(u'\xa0', u' ')

        try:
            salary = item.find('span', {'class': 'bloko-header-section-3'}).text

            salary = salary.split()

            if salary[0] == 'до':
                temp_dict['salary_min'] = None
                temp_dict['salary_max'] = int(f'{salary[1]}{salary[2]}')
                temp_dict['salary_currency'] = salary[3]
            elif salary[0] == 'от':
                temp_dict['salary_min'] = int(f'{salary[1]}{salary[2]}')
                temp_dict['salary_max'] = None
                temp_dict['salary_currency'] = salary[3]
            else:
                temp_dict['salary_min'] = (int(f'{salary[0]}{salary[1]}'))
                temp_dict['salary_max'] = (int(f'{salary[3]}{salary[4]}'))
                temp_dict['salary_currency'] = salary[5]

            if temp_dict['salary_currency'] == 'руб.':
                temp_dict['salary_currency'] = 'RUB'
        except AttributeError:
            temp_dict['salary_min'] = None
            temp_dict['salary_max'] = None
            temp_dict['salary_currency'] = None

        temp_dict['source'] = 'hh.ru'

        data_list.append(temp_dict)


objs = {'data': data_list}

# записываем полученные данные в json формате
with open('vacancies.json', 'w', encoding='utf-8') as f:
    json.dump(objs, f, indent=4, ensure_ascii=False)




