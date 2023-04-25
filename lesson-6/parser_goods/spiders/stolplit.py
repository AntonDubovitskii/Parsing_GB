import scrapy
from scrapy.http import HtmlResponse
from parser_goods.items import ParserGoodsItem
from scrapy.loader import ItemLoader


class StolplitSpider(scrapy.Spider):
    name = "stolplit"
    allowed_domains = ["stolplit.ru"]
    start_urls = [f"https://www.stolplit.ru/internet-magazin/katalog-mebeli/3387-krovati-140-sm/"]

    def parse(self, response: HtmlResponse):
        page_links = response.xpath("//div[@class='flex-layout__item js-product-info']/div/div/div[@class='append-slider-images']/a")
        for link in page_links:
            yield response.follow(link, callback=self.parse_goods)

    def parse_goods(self, response: HtmlResponse):
        loader = ItemLoader(item=ParserGoodsItem(), response=response)

        loader.add_xpath('name', '//h1/text()')
        loader.add_value('link', response.url)
        loader.add_xpath('images', "//a[@rel='gallery']/@href")
        loader.add_xpath('current_price', "//div[@id='js-detail_product_price_wrapper']/div[@class='price--current']/text()")
        loader.add_xpath('regular_price', "//div[@id='js-detail_product_price_wrapper']/div[@class='price--old']/text()")
        yield loader.load_item()


