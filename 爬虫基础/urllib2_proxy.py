import urllib2

http_proxy_handler = urllib2.ProxyHandler({"http":"118.212.137.135:31288"})

null_proxy_handler = urllib2.ProxyHandler()

proxySwitch = True

if proxySwitch:  
    opener = urllib2.build_opener(http_proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)

request = urllib2.Request("http://www.baidu.com/")

response = opener.open(request)

print response.read()