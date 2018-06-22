# coding=utf-8
import urllib
import urllib2

word = {"word":"百度"}

word = urllib.urlencode(word)

url = 'http://www.baidu.com/s' + '?' + word

headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

request = urllib2.Request(url,headers=headers)

print urllib2.urlopen(request).read().decode('utf-8')
