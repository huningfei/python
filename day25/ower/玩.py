import requests
from lxml import etree
import os

url = 'http://www.umei.cc/p/gaoqing/rihan/%s.htm'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

# 创建文件夹
if not os.path.exists('img'):
    os.mkdir('img')

page_start = int(input('enter start page:'))
page_end = int(input('enter end page:'))
for page in range(page_start, page_end + 1):
    print('正在下载第%d页图片' % page)
    new_url = format(url % page)
    # print(new_url)
    response = requests.get(url=new_url, headers=headers)
    page_text = response.text
    # 实例化一个etree对象，并且将页面数据放到etree

    tree = etree.HTML(page_text)
    div_list = tree.xpath('//div[@class="TypeList"]')

    # 写入到文件
    for div in div_list:
        img_url = div.xpath('//div[@class="TypeList"]//ul/li/a/img//@src')
        for eva_url in img_url:
            # print(eva_url)
            img_full_url=eva_url
            img_name=eva_url.split('/')[-1]
            img_data = requests.get(url=img_full_url, headers=headers).content
            img_path = 'img/' + img_name
            with open(img_path, 'ab')as f:
                f.write(img_data)
