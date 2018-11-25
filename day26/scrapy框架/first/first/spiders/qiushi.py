# -*- coding: utf-8 -*-
import scrapy


class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    # allowed_domains = ['www.aa.com']
    start_urls = ['https://www.qiushibaike.com/']

    def parse(self, response):
        # xpath为response中的方法，可以将xpath表达式直接作用于该函数中
        odiv = response.xpath('//div[@id="content-left"]/div')

        content_list = []  # 用于存储解析到的数据

        for div in odiv:
            # xpath函数返回的为列表，列表中存放的数据为Selector类型的数据。我们解析到的内容被封装在了Selector对象中，需要调用extract()函数将解析的内容从Selecor中取出。
            author = div.xpath('.//div[@class="author clearfix"]/a/h2/text()')[0].extract()

            content = div.xpath('.//div[@class="content"]/span/text()').extract()
            print(content)

            # 将解析到的内容封装到字典中
            dic = {
                '作者': author,
                '内容': content
            }
            # 将数据存储到content_list这个列表中
            content_list.append(dic)


        return content_list

# 运行方法在cmd里面,进去你所建的那个项目，
# 执行输出指定格式进行存储：将爬取到的数据写入不同格式的文件中进行存储
#     scrapy crawl qiubai -o qiubai.json
#     scrapy crawl qiubai -o qiubai.xml
#     scrapy crawl qiubai -o qiubai.csv

# #持久化存储方式：
#                 #1.基于终端指令：必须保证parse方法有一个可迭代类型对象的返回 ，content_list就是一个科迭代的
#                 #2.基于管道