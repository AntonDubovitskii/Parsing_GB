# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# from scrapy.loader.processors import Compose, MapCompose, TakeFirst
from itemloaders.processors import Compose, MapCompose, TakeFirst


def complete_url(link):
    """
    Формирование окончательного вида ссылки на изображение
    """
    link = 'https://stolplit.ru' + link
    return link


def clean_price(value):
    """
    Очистка строки с записью цены от лишних пробелов, а после - приведение к числовому типу
    """
    try:
        value = int(value[0].strip().replace(' ', ''))
    except:
        return value
    return value


def clean_title(value):
    """
    Очистка названия от множества лишних пробелов и переносов строки
    """
    try:
        value = value[0].strip()
    except:
        return value
    return value


class ParserGoodsItem(scrapy.Item):
    name = scrapy.Field(input_processor=Compose(clean_title), output_processor=TakeFirst())
    link = scrapy.Field(output_processor=TakeFirst())
    images = scrapy.Field(input_processor=MapCompose(complete_url))
    current_price = scrapy.Field(input_processor=Compose(clean_price), output_processor=TakeFirst())
    regular_price = scrapy.Field(input_processor=Compose(clean_price), output_processor=TakeFirst())
    _id = scrapy.Field()

