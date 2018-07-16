# _*_ coding:utf-8 _*_
__author__ = 'wang'
__date__ = '2018/6/22 10:14'

import urllib.request
import urllib.parse

data = bytes(urllib.parse.urlencode({'word':'百度'}),encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/get',data=data)
print(response.read())