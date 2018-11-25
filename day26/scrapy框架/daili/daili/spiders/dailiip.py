# -*- coding: utf-8 -*-
# 开启代理的流程：
# 1 在setting里面开启下载中间件
'''
DOWNLOADER_MIDDLEWARES = {
   'daili.middlewares.DailiDownloaderMiddleware': 543,
}
'''
# 2 在middlewares里面写上代理
'''
    def process_request(self, request, spider):
        # request参数表示的就是拦截到的请求对象
        request.meta['proxy'] = "https://151.106.15.3:1080"
'''


import scrapy


class DailiipSpider(scrapy.Spider):
    name = 'dailiip'
    # allowed_domains = ['www.xx.com']
    start_urls = ['https://www.baidu.com/s?wd=ip']

    def parse(self, response):
        page_text = response.text
        with open('./daili.html', 'w', encoding='utf-8') as fp:
            fp.write(page_text)
