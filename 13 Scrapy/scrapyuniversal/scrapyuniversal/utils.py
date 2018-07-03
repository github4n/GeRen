# _*_ coding:utf-8 _*_
__author__ = 'wang'
__date__ = '2018/6/30 21:37'

from os.path import realpath,dirname
import json


def get_config(name):
    path = dirname(realpath(__file__)) + '/configs/' + name + '.json'
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
