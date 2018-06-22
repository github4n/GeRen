# coding=utf-8

import requests

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

formdata = {
    "i": "喜欢",
	"from":"AUTO",
	"to":"AUTO",
	"smartresult": "dict",
	"client": "fanyideskweb",
	"salt": "1528165968770",
	"sign": "db15cde0b2a06a0874ebc4192c4e18d6",
	"doctype": "json",
	"version": "2.1",
	"keyfrom": "fanyi.web",
	"action": "FY_BY_CLICKBUTTION",
	"typoResult": "false"
}

response = requests.post(url,data = formdata,headers=headers)

print response.content