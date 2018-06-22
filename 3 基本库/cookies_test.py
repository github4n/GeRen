# _*_ coding:utf-8 _*_
__author__ = 'wang'
__date__ = '2018/6/22 11:06'

import http.cookiejar,urllib.request

cookies = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookies)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookies:
    print(item.name+ '=' +item.value)