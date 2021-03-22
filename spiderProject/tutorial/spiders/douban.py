# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath("//ol[@class='grid_view']/li/div[@class='item']")

        for movie in movie_list:
            item = TutorialItem()
            item['title'] = movie.xpath(".//div[@class='hd']/a/span[1]/text()").extract_first()
            item['url'] = movie.xpath(".//div[@class='hd']/a/@href").extract_first()
            item['description'] = movie.xpath(".//span[@class='inq']/text()").extract_first()
            yield item
