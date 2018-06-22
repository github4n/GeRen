# _*_ coding:utf-8 _*_
__author__ = 'wang'
__date__ = '2018/6/22 14:06'

import requests

r = requests.get('http://www.baidu.com')
print(r.status_code)
print (type(r))
print (type(r.cookies))