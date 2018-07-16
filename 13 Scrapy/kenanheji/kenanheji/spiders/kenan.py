# -*- coding: utf-8 -*-
import json

import scrapy
from urllib.parse import urlencode
from scrapy import Request,Spider

from kenanheji.items import KenanhejiItem


class KenanSpider(scrapy.Spider):
    name = 'kenan'

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
        # 'Referer': 'http://image.baidu.com/'
    }

    allowed_domains = ['http://image.baidu.com/']
    start_urls = ['http://image.baidu.com/search/acjson?']

# http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&queryWord=柯南&word=柯南&pn=30

    def parse(self, response):
        result = json.loads(response.text)
        for image in result.get('data'):
            item = KenanhejiItem()
            item['id'] = image.get('di')
            item['thumbURL'] = image.get('thumbURL')
            item['middleURL'] = image.get('middleURL')
            if image.get('replaceUrl'):
                item['FromURL'] = image.get('replaceUrl')[-1].get('FromURL')
            yield item

    def start_requests(self):
        data = {'tn': 'resultjson_com', 'ipn':'rj','queryWord':'柯南','word':'柯南'}
        base_url = 'http://image.baidu.com/search/acjson?'
        for page in range(2, self.settings.get('MAX_PAGE') + 1):
            data['pn'] = page * 30
            params = urlencode(data)
            url = base_url + params
            yield Request(url, self.parse,headers=self.headers)


