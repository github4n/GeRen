# coding=utf-8

import urllib2

headers = {

    "Host":"www.renren.com",
    "Connection":"keep-alive",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",

    # 便于终端阅读，表示不支持压缩文件
    # Accept-Encoding: gzip, deflate, sdch,

    # 重点：这个Cookie是保存了密码无需重复登录的用户的Cookie，这个Cookie里记录了用户名，密码(通常经过RAS加密)
    "Cookie": "anonymid=ji1c5881-rp8poj; depovince=LN; _r01_=1; JSESSIONID=abcoZnMpCfkaB4zC8Vopw; jebe_key=7d6e2064-6445-463b-a123-c34ad50b9a4f%7C767f399d0e255a7f3ae7bbf03d886cb2%7C1528182081558%7C1%7C1528182082907; jebecookies=87c78b5a-5cfd-447d-83d4-5d473ef4d4ea|||||; ick_login=4f6d3867-e0d1-4294-93e4-1c35e3159026; _de=327EA6C087A82E0C543E68E99FA3061F; p=ffc4f04204d7f995f310daa4bb9cd38b2; ap=486413432; first_login_flag=1; ln_uact=18840862253; ln_hurl=http://hdn.xnimg.cn/photos/hdn121/20130329/1220/h_main_UT13_3fe500001890113e.jpg; t=a52a00f37144805feb539f40aa091b882; societyguester=a52a00f37144805feb539f40aa091b882; id=486413432; xnsid=31400363; ver=7.0; loginfrom=null"
}

# 2. 通过headers里的报头信息（主要是Cookie信息），构建Request对象
request = urllib2.Request("http://www.renren.com/", headers = headers)

# 3. 直接访问renren主页，服务器会根据headers报头信息（主要是Cookie信息），判断这是一个已经登录的用户，并返回相应的页面
response = urllib2.urlopen(request)

# 4. 打印响应内容
print response.read()