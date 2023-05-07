# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Compose, MapCompose, TakeFirst


def clean_price(value):
    """
    Очистка строки с записью цены от лишних пробелов, а после - приведение к числовому типу
    """
    try:
        value = value[1].strip().replace(' ', '').replace('$', '')

    except:
        return value
    return int(float(value))


class ScrapyLoginItem(scrapy.Item):
    name = scrapy.Field(output_processor=TakeFirst())
    link = scrapy.Field(output_processor=TakeFirst())
    image = scrapy.Field(output_processor=TakeFirst())
    price_MSRP = scrapy.Field(input_processor=Compose(clean_price), output_processor=TakeFirst())
    _id = scrapy.Field()



