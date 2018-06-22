import urllib
import urllib2

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

formdata = {
    'start':'0',
    'limit':'10'
}

data = urllib.urlencode(formdata)

requese = urllib2.Request(url,data=data,headers=headers)

response = urllib2.urlopen(requese)

print response.read()
