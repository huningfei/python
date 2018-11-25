# 需求，爬取笑话网中的段子内容和作者
from lxml import etree
import requests

url = 'https://www.xiaohua.com/duanzi/'

headers = {
    #对UA进行重写操作（伪装）
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
response = requests.get(url=url,headers=headers)


page_text = response.text

# 实例化一个etree对象，并且将页面数据放到etree

tree = etree.HTML(page_text)
div_list = tree.xpath('//div[@class="content-left"]/div[@class="one-cont"]')
print(div_list)

# 写入到文件
fp = open('./xiaohua.txt', 'w', encoding='utf-8')
for div in div_list:
    # print(div)
    author = div.xpath('//div[@class="one-cont-font clearfix"]//i/text()')[0]
    # print(author)
    content = div.xpath('./p/a//text()')[0]
    print(content)
    fp.write(author + ":" + content + "\n\n")
fp.close()
