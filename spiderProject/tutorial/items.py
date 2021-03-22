# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()


class StockstarItemLoader(ItemLoader):
    #自定义itemloader,用于存储爬虫所抓取的字段内容
    default_output_processor = TakeFirst()


class StockstarItem(scrapy.Item):  # 建立相应的字段
    code = scrapy.Field()  # 股票代码
    abbr = scrapy.Field()  # 股票简称
    circulation_market_price = scrapy.Field()  # 流通市值(万元)
    total_market_price = scrapy.Field()  # 总市值(万元)
    tradable_equity = scrapy.Field()  # 流通股本(万元)
    total_equity = scrapy.Field()  # 总股本(万元)
