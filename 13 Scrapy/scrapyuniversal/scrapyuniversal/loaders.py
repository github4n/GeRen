# _*_ coding:utf-8 _*_
__author__ = 'wang'
__date__ = '2018/6/30 18:34'

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst,Join,Compose


class NewsLoader(ItemLoader):
    default_output_processor = TakeFirst()


class ChinaLoader(NewsLoader):
    text_out = Compose(Join(), lambda s: s.strip())
    source_out = Compose(Join(), lambda s: s.strip())