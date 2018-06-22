# _*_ coding:utf-8 _*_
__author__ = 'wang'
__date__ = '2018/6/22 15:39'

import requests
proxy = '222.185.137.101:6666'

proxies = {
    'http':'http://' + proxy,
    'https':'https://' + proxy,
}
try:
    response = requests.get('http://httpbin.org/get',proxies=proxies)
    print (response.text)

except requests.exceptions.ConnectionError as e:
    print ('Error',e.args)
