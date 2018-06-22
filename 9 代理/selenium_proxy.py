# _*_ coding:utf-8 _*_
__author__ = 'wang'
__date__ = '2018/6/22 15:27'

from selenium import webdriver

proxy = '222.185.137.101:6666'
# proxy = '115.223.234.113:9000'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://' + proxy)
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://httpbin.org/get')