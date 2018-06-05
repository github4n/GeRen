# coding=utf-8

import os
import urllib
import urllib2
from lxml import etree

class Spider(object):
    """docstring for Spider"""
    def __init__(self):
        super(Spider, self).__init__()
        self.tiebaName = raw_input('贴吧名：')
        self.beginPage = int(raw_input('请输入起始页：'))
        self.endPage = int(raw_input('请输入结束页：'))

        self.url = 'http://tieba.baidu.com/f'

        self.ua_header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}

        self.userName = 1


    def tiebaSpider(self):
        for page in range(self.beginPage,self.endPage+1):
            pn = (page -1) * 50
            word = {"pn":pn,
                    "kw":self.tiebaName
                }

        word = urllib.urlencode(word)

        url = self.url + '?' + word

        links = self.loadPage(url)

    def loadPage(self,url):
        request = urllib2.Request(url, headers=self.ua_header)
        html = urllib2.urlopen(request).read()

        selector=etree.HTML(html)

        links = selector.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')

        for link in links:
            link = "http://tieba.baidu.com" + link
            self.loadImages(link)

    def loadImages(self,link):
        request = urllib2.Request(link, headers = self.ua_header)
        html = urllib2.urlopen(request).read()
        selector = etree.HTML(html)
        imagesLinks = selector.xpath('//img[@class="BDE_Image"]/@src')

        for imagesLink in imagesLinks:
            self.writeImage(imagesLink)


    def writeImage(self,imagesLink):
        print imagesLink
        print "正在存储文件 %d ..." % self.userName
        # 1. 打开文件，返回一个文件对象
        file = open('./images/' + str(self.userName)  + '.png', 'wb')

        # 2. 获取图片里的内容
        images = urllib2.urlopen(imagesLink).read()

        # 3. 调用文件对象write() 方法，将page_html的内容写入到文件里
        file.write(images)

        # 4. 最后关闭文件
        file.close()

        # 计数器自增1
        self.userName += 1

if __name__ == '__main__':
    tiebaspider = Spider()
    tiebaspider.tiebaSpider()


























