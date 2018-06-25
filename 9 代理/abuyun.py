# _*_ coding:utf-8 _*_
__author__ = 'wang'
__date__ = '2018/6/25 08:58'


import requests

url = 'http://httpbin.org/get'

# 代理服务器
proxy_host = 'proxy.abuyun.com'
proxy_prot = '9020'

# 代理隧道验证信息
proxy_user = 'H765LK940252G5PD'
proxy_password = '09DEF36345EF3B15'

proxy_meta = 'http://%(user)s:%(pass)s@%(host)s:%(port)s' % {
    'host': proxy_host,
    'port': proxy_prot,
    'user': proxy_user,
    'pass': proxy_password,
}

headers = {
            "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
        }
proxies = {
    'http':proxy_meta,
    'https':proxy_meta,
}

response = requests.get(url,headers=headers,proxies=proxies)

print(response.status_code)
print(response.text)