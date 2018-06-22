# coding=utf-8

import urllib
import urllib2

def tiebaSpider(url,beginPage,endPage):
	    for page in range(beginPage, endPage + 1):
	        pn = (page - 1) * 50

	        filename = "第" + str(page) + "页.html"
	        # 组合为完整的 url，并且pn值每次增加50
	        fullurl = url + "&pn=" + str(pn)
	        #print fullurl

	        # 调用loadPage()发送请求获取HTML页面
	        html = loadPage(fullurl, filename)
	        # 将获取到的HTML页面写入本地磁盘文件
	        writeFile(html, filename)

def loadPage(url, filename):
    '''
        作用：根据url发送请求，获取服务器响应文件
        url：需要爬取的url地址
        filename: 文件名
    '''
    print "正在下载" + filename

    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    return response.read()

def writeFile(html, filename):
    """
        作用：保存服务器响应文件到本地磁盘文件里
        html: 服务器响应文件
        filename: 本地磁盘文件名
    """
    print "正在存储" + filename
    with open(filename, 'w') as f:
        f.write(html)
    print "-" * 20

if __name__ == "__main__":

    kw = raw_input("请输入需要爬取的贴吧:")
    # 输入起始页和终止页，str转成int类型
    beginPage = int(raw_input("请输入起始页："))
    endPage = int(raw_input("请输入终止页："))

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw" : kw})

    # 组合后的url示例：http://tieba.baidu.com/f?kw=lol
    url = url + key
    tiebaSpider(url, beginPage, endPage)