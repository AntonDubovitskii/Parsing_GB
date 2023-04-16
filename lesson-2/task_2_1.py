"""
Задание:

Написать приложение или функцию, которые собирают основные новости с сайта на выбор: lenta.ru, yandex-новости.
Для парсинга использовать XPath.

Структура данных в виде словаря должна содержать:

- название источника;
- наименование новости;
- ссылку на новость;
- дата публикации.

"""
import json
from lxml import html
import requests


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
        data_dict['date'] = (html.fromstring(requests.get(data_dict['link'], headers=headers).text))\
            .xpath("//a[@class='topic-header__item topic-header__time']/text()")[0]

        data_list.append(data_dict)
        print(data_dict)
    # Иногда на ленте добавляют новости со ссылками на другие ресурсы, их игнорируем
    except requests.exceptions.ConnectionError:
        continue

objs = {'data': data_list}

# записываем полученные данные в json формате
with open('news_parse.json', 'w', encoding='utf-8') as f:
    json.dump(objs, f, indent=4, ensure_ascii=False)

