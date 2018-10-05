# _*_ coding:utf-8 _*_
__author__ = 'wang'
__date__ = '2018/7/5 14:37'

import requests
from lxml import etree
import json

page = 1
url = 'http://www.qiushibaike.com/8hr/page/' + str(page)

try:
    headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    resHtml = response.text

    html = etree.HTML(resHtml)
    result = html.xpath('//div[contains(@id,"qiushi_tag")]')

    item = {}

    for site in result:

        imgUrl = site.xpath('./div/a/img/@src')[0]
        username = site.xpath('.//h2')[0].text
        content = site.xpath('.//div[@class="content"]/span')[0].text.strip()
        # 投票次数
        votes = site.xpath('.//*[@class="number"]')[0].text
        # 评论信息
        comments = site.xpath('.//i')[1].text

        item = {
            "imgUrl":imgUrl,
            "username":username,
            "content":content,
            "votes":votes,
            "comments":comments
        }
        with open('qiushi.json','a',encoding='utf-8') as f:
            f.write(json.dumps(item,ensure_ascii=False) )

except Exception as e:
    print (e)