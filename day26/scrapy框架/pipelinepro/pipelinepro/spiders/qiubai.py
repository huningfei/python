#执行方式 ，进入到项目的文件夹下，在执行scrapy crawl qiubai  --nolog

# -*- coding: utf-8 -*-
import scrapy

from pipelinepro.items import PipelineproItem
class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xx.com']
    start_urls = ['https://www.qiushibaike.com/']

    def parse(self, response):
        # xpath返回的列表元素类型为Selecor类型
        div_list = response.xpath('//div[@id="content-left"]/div')
        # 声明一个用于存储解析到数据的列表
        all_data = []

        for div in div_list:
            # extract()可以将selector对象中存储的文本内容获取
            # author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            content = div.xpath('.//div[@class="content"]/span//text()').extract()
            content = "".join(content)

            # 实例化item对象
            item = PipelineproItem()
            # 将解析到的数据值存储到item对象中
            item['author'] = author
            item['content'] = content

            # 将item对象提交给管道
            yield item

        # 持久化存储方式：
        # 1.基于终端指令：必须保证parse方法有一个可迭代类型对象的返回
        # 2.基于管道:
        # 1.items.py:对该文件中的类进行实例化操作（item对象：存储解析到的数据值）。
        # 2.pipeline.py:管道，作用就是接受爬虫文件提交的item对象，然后将该对象中的数据值进行持久化存储操作
