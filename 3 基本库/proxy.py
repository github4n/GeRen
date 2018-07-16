# _*_ coding:utf-8 _*_
__author__ = 'wang'
__date__ = '2018/7/5 13:13'

import urllib.request
import random

# 代理可能失效，多试几次
proxy_list = [
    {"http" : "117.36.103.170:8118"},
    {"http" : "125.122.171.225:808"},
    {"http" : "118.190.95.26:9001"},
    {"http" : "221.224.49.237:3128"},
    {"http" : "122.235.174.124:8118"}
]

# 随机选择一个代理
proxy = random.choice(proxy_list)
# 使用选择的代理构建代理处理器对象
httpproxy_handler = urllib.request.ProxyHandler(proxy)

opener = urllib.request.build_opener(httpproxy_handler)

request = urllib.request.Request("http://httpbin.org/get")
response = opener.open(request)
print (response.read().decode('utf-8'))