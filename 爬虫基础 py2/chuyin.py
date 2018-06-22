import requests
from lxml import etree

for i in range(1,4):
	url_link = 'http://www.mmonly.cc/tag/cywl/' + str(i) + '.html'

	headers = {
	    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
	}
	print(url_link)
	html = requests.get(url_link,headers=headers).text

	html = etree.HTML(html)

	urls = html.xpath("//div[@class='item_list infinite_scroll masonry']//img/@src")

	# print(urls)

	for url in urls:

	    # print(url)

	    try:
	        filename = url[-10:]
	        print(u'开始下载图片:%s'%filename)
	        with open(filename, "wb+") as jpg:
	            jpg.write(requests.get(url, headers=headers).content)
	    except:
	        pass












