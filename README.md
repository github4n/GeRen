# Python3网络爬虫开发实战
## 50 directories, 179 files

````
.
├── 1 开发环境
│   └── requirements.txt
├── 2 爬虫基础 py2
│   ├── chuyin.py
│   ├── kennan.py
│   ├── py_mongodb.py
│   ├── py_mysql.py
│   ├── request.py
│   ├── request_post.py
│   ├── requests_proxy.py
│   ├── tiebaSpider.py
│   ├── tieba_xpath.py
│   ├── urllib2_ajax.py
│   ├── urllib2_cookielibtest1.py
│   ├── urllib2_get.py
│   ├── urllib2_proxy.py
│   ├── urllib2_request.py
│   ├── urllib2_urlopen.py
│   ├── urllib_cookies.py
│   ├── urllib_opener.py
│   ├── xiaoqinxin.py
│   ├── youdao.py
│   └── zhihu_explore.py
├── 3 基本库
│   ├── 3.4 猫眼电影排行榜.py
│   ├── cookies_test.py
│   ├── requests_test.py
│   ├── result.txt
│   └── urllib_test.py
├── 5 数据库
│   ├── redis_data.json
│   └── redis_test.py
├── 6 ajax
│   ├── jiepai.py
│   └── weibo.py
├── 7 动态渲染页面爬取
│   ├── render_html.py
│   ├── selenium.test2.py
│   ├── selenium_test.py
│   └── taobao.py
├── 8 验证码
│   ├── captcha1.png
│   ├── captcha2.png
│   ├── code_tesserocr.py
│   ├── geestest.py
│   ├── images.png
│   └── weibo.py
├── 9 代理
│   ├── PhantomJS_proxy.py
│   ├── abuyun.py
│   ├── requests_proxy.py
│   ├── selenium_proxy.py
│   ├── weixin
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── db.py
│   │   ├── mysql.py
│   │   ├── request.py
│   │   └── spider.py
│   └── 代理池
│       ├── __init__.py
│       ├── api.py
│       ├── crawler.py
│       ├── db.py
│       ├── error.py
│       ├── getter.py
│       ├── scheduler.py
│       ├── tester.py
│       └── utils.py
├── 10 模拟登录
│   ├── CookiesPool
│   │   ├── README.md
│   │   ├── cookiespool
│   │   │   ├── __init__.py
│   │   │   ├── api.py
│   │   │   ├── config.py
│   │   │   ├── db.py
│   │   │   ├── generator.py
│   │   │   ├── importer.py
│   │   │   ├── scheduler.py
│   │   │   └── tester.py
│   │   ├── importer.py
│   │   ├── login
│   │   │   ├── __init__.py
│   │   │   └── weibo
│   │   │       ├── __init__.py
│   │   │       ├── cookies.py
│   │   │       └── templates
│   │   │           ├── 1234.png
│   │   │           ├── 1243.png
│   │   │           ├── 1324.png
│   │   │           ├── 1342.png
│   │   │           ├── 1423.png
│   │   │           ├── 1432.png
│   │   │           ├── 2134.png
│   │   │           ├── 2143.png
│   │   │           ├── 2314.png
│   │   │           ├── 2341.png
│   │   │           ├── 2413.png
│   │   │           ├── 2431.png
│   │   │           ├── 3124.png
│   │   │           ├── 3142.png
│   │   │           ├── 3214.png
│   │   │           ├── 3241.png
│   │   │           ├── 3412.png
│   │   │           ├── 3421.png
│   │   │           ├── 4123.png
│   │   │           ├── 4132.png
│   │   │           ├── 4213.png
│   │   │           ├── 4231.png
│   │   │           ├── 4312.png
│   │   │           └── 4321.png
│   │   ├── requirements.txt
│   │   └── run.py
│   └── github_login.py
├── 11 App的爬取
│   ├── dedao.py
│   ├── dedao_test.py
│   ├── moments_weixin.py
│   ├── script.py
│   └── weixin_login.text.py
├── 12 pyspider框架
│   └── data
│       ├── project.db
│       ├── result.db
│       ├── scheduler.1d
│       ├── scheduler.1h
│       ├── scheduler.all
│       └── task.db
├── 13 Scrapy
│   ├── images360
│   │   ├── images360
│   │   │   ├── __init__.py
│   │   │   ├── images
│   │   │   ├── items.py
│   │   │   ├── middlewares.py
│   │   │   ├── pipelines.py
│   │   │   ├── settings.py
│   │   │   └── spiders
│   │   │       ├── __init__.py
│   │   │       └── images.py
│   │   └── scrapy.cfg
│   ├── meixi
│   │   ├── meixi
│   │   │   ├── __init__.py
│   │   │   ├── images
│   │   │   ├── items.py
│   │   │   ├── middlewares.py
│   │   │   ├── pipelines.py
│   │   │   ├── settings.py
│   │   │   └── spiders
│   │   │       ├── __init__.py
│   │   │       └── images.py
│   │   └── scrapy.cfg
│   ├── scrapydownloadertest
│   │   ├── scrapy.cfg
│   │   └── scrapydownloadertest
│   │       ├── __init__.py
│   │       ├── items.py
│   │       ├── middlewares.py
│   │       ├── pipelines.py
│   │       ├── settings.py
│   │       └── spiders
│   │           ├── __init__.py
│   │           └── httpbin.py
│   ├── scrapyseleniumtest
│   │   ├── ghostdriver.log
│   │   ├── scrapy.cfg
│   │   └── scrapyseleniumtest
│   │       ├── __init__.py
│   │       ├── items.py
│   │       ├── middlewares.py
│   │       ├── pipelines.py
│   │       ├── settings.py
│   │       └── spiders
│   │           ├── __init__.py
│   │           └── taobao.py
│   ├── scrapysplashtest
│   │   ├── scrapy.cfg
│   │   └── scrapysplashtest
│   │       ├── __init__.py
│   │       ├── items.py
│   │       ├── middlewares.py
│   │       ├── pipelines.py
│   │       ├── settings.py
│   │       └── spiders
│   │           ├── __init__.py
│   │           └── taobao.py
│   ├── scrapyuniversal
│   │   ├── logs
│   │   ├── run.py
│   │   ├── scrapy.cfg
│   │   └── scrapyuniversal
│   │       ├── __init__.py
│   │       ├── configs
│   │       │   └── china.json
│   │       ├── items.py
│   │       ├── loaders.py
│   │       ├── middlewares.py
│   │       ├── pipelines.py
│   │       ├── rules.py
│   │       ├── settings.py
│   │       ├── spiders
│   │       │   ├── __init__.py
│   │       │   ├── china.py
│   │       │   └── universal.py
│   │       ├── urls.py
│   │       └── utils.py
│   └── tutorial
│       ├── Dockerfile
│       ├── logs
│       │   ├── quote
│       │   └── quotes
│       │       ├── 2018-07-03T195214.024170.log
│       │       └── 2018-07-03T195624.455819.log
│       ├── requirements.txt
│       ├── scrapy.cfg
│       └── tutorial
│           ├── __init__.py
│           ├── items.py
│           ├── middlewares.py
│           ├── pipelines.py
│           ├── settings.py
│           └── spiders
│               ├── __init__.py
│               └── quotes.py
├── 14 Scrapy redis分布式
├── 15 scrapy 部署
├── README.md
```

 tree -NIv __pycache__  > README.md
