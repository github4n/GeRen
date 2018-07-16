import urllib.request
import urllib.parse

data = urllib.parse.urlencode({'wd':'百度'})

url  = 'http://wwww.baidu.com/s?' + data

response = urllib.request.urlopen(url)

print(response.read().decode('utf-8'))

