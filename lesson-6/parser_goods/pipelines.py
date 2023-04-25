# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pathlib import PurePath
from urllib.parse import urlparse

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import scrapy
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline


class ParserGoodsPipeline:
    def __init__(self):
        client = MongoClient('localhost:27017')
        self.mongo_db = client.parser_goods

    def process_item(self, item, spider):
        collection = self.mongo_db[spider.name]
        collection.insert_one(item)

        return item


class StolplitImagesPipline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['images']:
            for img in item['images']:
                try:
                    yield scrapy.Request(img)
                except TypeError as e:
                    print(e)

    def item_completed(self, results, item, info):
        if results:
            item['images'] = [itm[1] for itm in results if itm[0]]
        return item

    def file_path(self, request, response=None, info=None, *, item=None):
        dir = f'{item["name"]}/'.replace(',', ' ').replace(' ', '_')
        return dir + PurePath(urlparse(request.url).path).name

