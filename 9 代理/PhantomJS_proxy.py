# _*_ coding:utf-8 _*_
__author__ = 'wang'
__date__ = '2018/6/22 15:54'

from selenium import webdriver

service_args = [
    '--proxy=222.185.137.101:6666',
    '--proxy-type=http'
]
browser = webdriver.PhantomJS(service_args=service_args)
browser.get('http://httpbin.org/get')
print (browser.page_source)