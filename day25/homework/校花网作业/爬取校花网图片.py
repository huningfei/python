import requests
from lxml import etree
import os

path = r'D:\python21\python\day25\homework\校花网作业'
# 获取url
url = 'http://www.521609.com/daxuemeinv/list%s.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

# 创建文件夹
if not os.path.exists('img'):
    os.mkdir('img')

for page in range(81, 824):
    print('正在下载第%d页图片' % page)
    new_url = format(url % page)
    # print(new_url)
    response = requests.get(url=new_url, headers=headers)
    page_text = response.text
    # 实例化一个etree对象，并且将页面数据放到etree

    tree = etree.HTML(page_text)
    div_list = tree.xpath('//div[@class="index_img list_center"]/ul//li')
    # print(div_list)

    # 写入到文件
    for div in div_list:
        img_url = div.xpath('//div[@class="index_img list_center"]//li/a//@src')
        # print(img_url)
        for eve_url in img_url:
            img_full_url = 'http://www.521609.com' + eve_url
            img_data = requests.get(url=img_full_url, headers=headers,timeout = 500).content
            img_name = img_full_url.split('/')[-1]
            img_path = 'img/' + img_name
            with open(img_path, 'ab')as f:
                f.write(img_data)


