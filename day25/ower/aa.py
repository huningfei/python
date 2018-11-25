import requests
from lxml import etree
import os

url = 'https://www.btzhizhu.org/search-%E4%BD%90%E4%BD%90%E6%9C%A8%E5%B8%8C-video-create_time-1.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

# 创建文件夹
if not os.path.exists('vadeio'):
    os.mkdir('vadeio')

response = requests.get(url=url, headers=headers)
page_html=response.text
# print(data)

# 实例化一个etree对象，并且将页面数据放到etree

tree = etree.HTML(page_html)

url_list = tree.xpath('.//div[@class="table"]//div[@class=" xh-highlight"]')
print(url_list)
# for url in url_list:
#     # print(url)
#     all_url = url.xpath('/html/body/div[1]/table/tbody//tr//a')[0]
#     print(all_url)

# print(all_url)
# print(all_url)
# for url in all_url:
#     print(url)
