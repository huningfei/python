# -*- coding: utf-8 -*-
import scrapy


class LoginpostSpider(scrapy.Spider):
    name = 'loginpost'
    # allowed_domains = ['www.xx.com']
    start_urls = ['https://accounts.douban.com/login']

    def start_requests(self):
        data = {
            'source': 'movie',
            'redir': 'https://movie.douban.com/',
            'form_email': '15027900535',
            'form_password': 'bobo@15027900535',
            'login': '登录',
        }
        for url in self.start_urls:  # 登录页面
            yield scrapy.FormRequest(url=url,callback=self.parse,formdata=data) # FormRequest发送的是post请求

    def getPageText(self, response): # 这个是用来解析个人主页的数据的

        page_text = response.text
        with open('./douban.html', 'w', encoding='utf-8') as fp:
            fp.write(page_text)
            print('over')
    def parse(self, response):
        # 对当前用户的个人主页页面进行获取
        url = 'https://www.douban.com/people/185687620/'
        yield scrapy.Request(url=url, callback=self.getPageText)
