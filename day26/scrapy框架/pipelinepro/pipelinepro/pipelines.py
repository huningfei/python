# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class PipelineproPipeline(object):
    # 作用：每当爬虫文件向管道提交一次item，该方法就会被调用一次。item参数就是接受到爬虫文件给提交过来的item对象
    # 该方法只有在开始爬虫的时候被调用一次
    fp = None

    def open_spider(self, spider):
        print('开始爬虫')
        self.fp = open('./qiubai_data.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author + ":" + content)
        return item

    # 该方法只有在爬虫结束后被调用一次
    def close_spider(self, spider):
        print('爬虫结束')
        self.fp.close()

# 这个是写入mysql数据库 的  create table qiubai (author varchar(100),content varchar(9999));  创建表
class MyPipeline(object):
    conn = None
    cursor = None

    # 作用：每当爬虫文件向管道提交一次item，该方法就会被调用一次。item参数就是接受到爬虫文件给提交过来的item对象
    def open_spider(self, spider):
        self.conn = pymysql.Connect(host="127.0.0.1", port=3306, db="scrapydb", charset="utf8", user="root",password="123")
        self.cursor = self.conn.cursor()
        print('mysql')

    def process_item(self, item, spider):
        author = item['author']
        content = item['content']

        sql = "insert into qiubai values('%s','%s')" % (author, content)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

