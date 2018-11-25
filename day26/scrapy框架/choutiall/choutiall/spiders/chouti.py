# -*- coding: utf-8 -*-
import scrapy

from choutiall.items import ChoutiallItem
class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://dig.chouti.com/r/pic/hot/1']
    # 设计一个所有页码通用的url
    url='https://dig.chouti.com/r/pic/hot/%d'
    pageNum=1
    def parse(self, response):

        div_list = response.xpath('//div[@class="content-list"]/div')
        for div in div_list:
            title = div.xpath('./div[3]/div[1]/a/text()').extract_first()
            item = ChoutiallItem() # 实例化items
            item['title'] = title # 列表形式

            yield item

        # 进行其他页码对应url的请求操作
        if self.pageNum <= 120:

            self.pageNum += 1
            url = format(self.url % self.pageNum)
            # print(url)
            # 进行手动请求的发送
            yield scrapy.Request(url=url, callback=self.parse) #调用上面的parse方法去解析所有的页面

