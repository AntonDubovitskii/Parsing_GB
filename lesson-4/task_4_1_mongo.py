"""
Задание из методички:

1.	Сохранить данные из предыдущего домашнего задания в файл .json или .csv.
2.	Создать MongoDB, записать данные туда (любое название базы, любое название коллекции).
    Выполнить команду для демонстрации содержимого коллекции. Прикрепить скриншот.
3.	Создать базу данных sqlite, загрузить туда данные из парсера с предыдущего урока. Загрузить файл .db

Задание с сайта:

1. Написать приложение, которое собирает основные новости с сайта на выбор news.mail.ru, lenta.ru, yandex-новости.
Для парсинга использовать XPath. Структура данных должна содержать:
- название источника;
- наименование новости;
- ссылку на новость;
- дата публикации.

2. Сложить собранные новости в БД

"""
from pprint import pprint

import requests
from lxml import html
from pymongo import MongoClient


def parse_lenta():
    url = 'https://lenta.ru'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/111.0.0.0 Safari/537.36',
    }

    response = requests.get(url, headers=headers)

    dom = html.fromstring(response.text)
    news_list = dom.xpath("//a[contains(@class, '_topnews')]")

    data_list = []

    for count, article in enumerate(news_list):
        try:
            data_dict = {}

            data_dict['source'] = 'lenta.ru'
            if count == 0:
                # Первая новость находится в отдельном контейнере, поэтому приходится парсить отдельно
                data_dict['title'] = article.xpath(".//div/h3/text()")[0]
            else:
                data_dict['title'] = article.xpath(".//div/span/text()")[0]
            data_dict['link'] = f'{url}{article.xpath(f".//@href")[0]}'
            # На "Ленте" нет даты публикации на главной странице, поэтому приходится извлекать её из самой статьи
            data_dict['date'] = (html.fromstring(requests.get(data_dict['link'], headers=headers).text)) \
                .xpath("//a[@class='topic-header__item topic-header__time']/text()")[0]

            data_list.append(data_dict)
        # Иногда на ленте добавляют новости со ссылками на другие ресурсы, их игнорируем
        except requests.exceptions.ConnectionError:
            continue
    return data_list


def write_to_db():
    data = parse_lenta()
    db.news.insert_many(data)

    news = db.news.find()
    list_news = list(news)
    pprint(list_news)
    print(len(list_news))


client = MongoClient('mongodb://localhost:27017/')
db = client.news_db

if __name__ == '__main__':
    db.news.drop()
    write_to_db()





