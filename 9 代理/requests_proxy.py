# _*_ coding:utf-8 _*_
__author__ = 'wang'
__date__ = '2018/6/22 15:39'

import requests
proxy = '77.79.149.199:53281'

proxies = {
    'http':'http://' + proxy,
    'https':'https://' + proxy,
}
try:
    response = requests.get('http://httpbin.org/get',proxies=proxies)
    print (response.text)

except requests.exceptions.ConnectionError as e:
    print ('Error',e.args)
