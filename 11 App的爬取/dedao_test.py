# _*_ coding:utf-8 _*_
__author__ = 'wang'
__date__ = '2018/6/26 10:40'


def response(flow):
    print(flow.request.url)
    print(flow.request.text)