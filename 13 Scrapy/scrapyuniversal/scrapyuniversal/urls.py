# _*_ coding:utf-8 _*_
__author__ = 'wang'
__date__ = '2018/7/3 19:30'

def china(start, end):
    for page in range(start, end + 1):
        yield 'http://tech.china.com/articles/index_' + str(page) + '.html'
