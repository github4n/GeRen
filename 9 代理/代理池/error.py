# _*_ coding:utf-8 _*_
__author__ = 'wang'
__date__ = '2018/6/24 17:20'

class PoolEmptyError(Exception):

    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr('代理池已经枯竭')
