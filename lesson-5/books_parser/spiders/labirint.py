import scrapy
from scrapy.http import HtmlResponse
from books_parser.items import BooksParserItem


class LabirintSpider(scrapy.Spider):
    name = "labirint"
    allowed_domains = ["labirint.ru"]
    start_urls = ["https://www.labirint.ru/books/"]

    def parse(self, response:HtmlResponse):
        next_page = response.xpath("//div[@class='pagination-next']/a/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        books_links = response.xpath("(//div[@class='genres-carousel__container  products-row '])[2]"
                                     "/div[@class='genres-carousel__item']"
                                     "/div/div/a[@class='product-title-link']/@href").getall()
        for link in books_links:
            yield response.follow(link, callback=self.parse_book_details)

    def parse_book_details(self, response:HtmlResponse):
        book_url = response.url
        book_name = response.xpath("//div[@id='product-about']/h2/text()").get().split('"')[1]
        book_author = response.xpath("//div[@class='authors']/a/text()").get()
        book_price = int(response.xpath("//span[@class='buying-priceold-val-number']/text()").get())
        book_discount_price = int(response.xpath("//span[@class='buying-pricenew-val-number']/text()").get())
        book_rating = float(response.xpath("//div[@id='rate']/text()").get())

        yield BooksParserItem(
            url=book_url,
            name=book_name,
            author=book_author,
            price=book_price,
            discount_price=book_discount_price,
            rating=book_rating
        )
