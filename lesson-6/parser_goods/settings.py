# Scrapy settings for parser_goods project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "parser_goods"

SPIDER_MODULES = ["parser_goods.spiders"]
NEWSPIDER_MODULE = "parser_goods.spiders"

LOG_ENABLED = True
LOG_LEVEL = "DEBUG"

MEDIA_ALLOW_REDIRECTS = True

IMAGES_STORE = 'images'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
    # 'cookie':'qrator_jsid=1682330142.414.dGfHUv43TyrvkfXo-2m99h94ujeqlvgr5cueg5gu7pm9urkb5; '
    #          '_ym_uid=1670679841178962704; _ym_d=1682330144; _ym_isad=1; ggr-widget-test=0; '
    #          'cookie_accepted=true; tmr_lvid=f70e14b8377df28cddd97117daffabc3; tmr_lvidTS=1670679841573; '
    #          '_singleCheckout=true; _unifiedCheckout=true; _clientTypeInBasket=true; '
    #          '_gaexp=GAX1.2.IUgFRjY7S7qnkK4uRsCZRw.19540.2; x-api-option=srch-2705-default; '
    #          'aplaut_distinct_id=oxKMUlhzJSg9; iap.uid=e4de8f5c13f8494f85f7ca5bad2a873f; '
    #          '_gid=GA1.2.799066354.1682330145; GACookieStorage=GA1.2.1119422491.1682330144; '
    #          'sawOPH=true; _slfs=1682330560239; _slid=644653c018bdebf97d09319c; '
    #          '_slsession=32E09380-331E-4ED4-9EE6-0A96D826FEF9; X-API-Experiments-sub=B; '
    #          '_regionID=34; _gat_UA-20946020-1=1; storageForShopListActual=true; _ga=GA1.2.1119422491.1682330144; '
    #          'lastConfirmedRegionID=34; _ga_Z72HLV7H6T=GS1.1.1682330144.1.1.1682330691.0.0.0',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "parser_goods.middlewares.ParserGoodsSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "parser_goods.middlewares.ParserGoodsDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "parser_goods.pipelines.ParserGoodsPipeline": 300,
    "parser_goods.pipelines.StolplitImagesPipline": 200,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
