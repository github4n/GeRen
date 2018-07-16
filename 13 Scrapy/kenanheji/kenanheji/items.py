# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field


class KenanhejiItem(scrapy.Item):
    collection = 'kenan'
    id = Field()
    thumbURL = Field()
    middleURL = Field()
    FromURL = Field()


