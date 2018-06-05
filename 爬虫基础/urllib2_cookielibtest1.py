import urllib2
import cookielib

cookiejar = cookielib.CookieJar()

handler=urllib2.HTTPCookieProcessor(cookiejar)

opener = urllib2.build_opener(handler)

opener.open("http://www.baidu.com")

cookieStr = ""
for item in cookiejar:
    cookieStr = cookieStr + item.name + "=" + item.value + ";"

print cookieStr[:-1]


