# _*_ coding:utf-8 _*_
__author__ = 'wang'
__date__ = '2018/6/30 21:55'

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

rules = {
    'china':(
        Rule(LinkExtractor(allow='article\/.*\.html', restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'),
             callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(., "下一页")]'))
    )
}