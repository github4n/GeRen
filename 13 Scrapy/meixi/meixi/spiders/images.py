# -*- coding: utf-8 -*-
import scrapy
import json
from meixi.items import MeixiItem


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://image.so.com/j?q=%E6%A2%85%E8%A5%BF']

    def parse(self, response):
        result = json.loads(response.text)
        for image in result.get('list'):
            item = MeixiItem()
            item['id']  = image.get('id')
            item['url'] = image.get('img')
            item['title'] = image.get('title')
            item['thumb'] = image.get('thumb')
            yield item



