# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ChoutiallPipeline(object):
    fp = None

    def open_spider(self, spider):
        print('开始爬虫')
        self.fp = open('./chouti.txt', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        title = item['title']
        self.fp.write(title)
        return item

      # 该方法只有在爬虫结束后被调用一次

    def close_spider(self, spider):
        print('爬虫结束')
        self.fp.close()
