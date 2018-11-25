# 作业要求2.实现糗事百科中文字板块中的所有页面的指定数据（段子内容和作者名称也头像url）爬取

import requests
from lxml import etree
import os

# 获取url
url = 'https://www.qiushibaike.com/text/page/%s/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}
# 指定起始也结束页码
page_start = int(input('enter start page:'))
page_end = int(input('enter end page:'))

# 创建文件夹
if not os.path.exists('qiutu'):
    os.mkdir('qiutu')
# 循环解析且下载指定页码中的图片数据

for page in range(page_start, page_end + 1):
    print('正在下载第%d页图片' % page)
    new_url = format(url % page)
    # print(new_url)
    # response = requests.get(url=new_url, headers=headers,proxies={"https": '43.225.34.66:51505'})
    response = requests.get(url=new_url, headers=headers)
    page_text = response.text
    # 实例化一个etree对象，并且将页面数据放到etree

    tree = etree.HTML(page_text)
    div_list = tree.xpath('//div[@id="content-left"]/div')

    # print(div_list)
    # 写入到文件
    for div in div_list:
        # 头像
        avatars_url = div.xpath('//div[@class="author clearfix"]/a/img/@src')
        for avatars in avatars_url:
            avatars_full_url = 'https:' + avatars

        # 内容
        content = div.xpath('.//div[@class="content"]/span//text()')# 获取到多个
        content="".join(content) # 转换成字符串
        # print(content+'\n')
        # 作者
        author = div.xpath('.//div[@class="author clearfix"]//h2//text()')[0]
        # print(author)
        with open('xiaohua.txt', 'a', encoding='utf-8') as f:
            f.write(avatars_full_url + "\n" + author + ':' + content + "\n\n")


