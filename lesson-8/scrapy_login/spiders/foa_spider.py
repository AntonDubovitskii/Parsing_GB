import scrapy
from scrapy.loader import ItemLoader

from scrapy_login.items import ScrapyLoginItem


class FoaSpiderSpider(scrapy.Spider):
    name = "foa-spider"
    allowed_domains = ["foagroup.com"]
    start_urls = ["https://www.foagroup.com/customer/account/login/"]

    login = 'nosida1911@soombo.com'
    password = 'Djko3829ne'

    def parse(self, response):
        # Находим на странице токен и сохраняем в переменную
        token = response.xpath('//input[@name="form_key"]/@value').get()

        # Логинимся с помощью scrapy
        yield scrapy.FormRequest("https://www.foagroup.com/customer/account/loginPost/",
                                 formdata={'form_key': token, 'login[password]': self.password,
                                           'login[username]': self.login, 'send': ''},
                                 callback=self.verify_login)

    def verify_login(self, response):
        # Выводим в консоль данные, находящиеся на странице при успешной аутентификации
        # и переходим на страницу вишлиста профиля (товары туда добавлены заранее)
        account_info = response.xpath('//div[@class="grid_5 alpha"]/div/div/p/text()').getall()
        wishlist_link = response.xpath('//div[@class="wishlist-save with-search"]/a/@href').get()

        print(f"*****************{account_info[0].strip()} {account_info[1].replace(' ', '').strip()}*****************")

        yield response.follow(wishlist_link, callback=self.parse_wishlist)

    def parse_wishlist(self, response):
        # Проходимся по товарам в вишлисте и передаем их ссылки дальше
        page_links = response.xpath("//h3/a")
        for link in page_links:
            yield response.follow(link, callback=self.wishlist_details)

    def wishlist_details(self, response):
        # Парсим называние, ссылку, изображение и цену каждого товара
        loader = ItemLoader(item=ScrapyLoginItem(), response=response)

        loader.add_xpath('name', '//div[@class="products-name"]/h2/text()')
        loader.add_value('link', response.url)
        loader.add_xpath('image', "//p[@class='product-image']/a/@href")
        loader.add_xpath('price_MSRP',
                         "//span[@class='regular-price']/span/text()")

        yield loader.load_item()


