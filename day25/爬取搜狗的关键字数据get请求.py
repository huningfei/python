import requests

#######################爬取的结果是一个网页，基础版
'''
# 指定url
url='https://www.sogou.com/web?query=%E9%AD%8F%E6%8C%AF%E6%B5%B7&'
# 发起请求
response=requests.get(url=url)
# 获取响应对象中的数据值
page_text=response.text
# 存储到硬盘
with open('./weizhenhai.html','w',encoding='utf-8')as f:
    f.write(page_text)
'''

########################优化版，也是爬取一个网页
# 指定搜索关键字
word=input('please input a word you want search:')
# 指定url

url = 'https://www.sogou.com/web?'
# 自定义请求头信息,防止目标网站设置防爬策略
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
# 封装get请求参数
prams = {
    'query': word,

}
# 发起请求
response = requests.get(url=url,params=prams)

# 获取响应数据
page_text=response.text

# 持久化存储
with open('./baidu.html','w',encoding='utf-8') as f:
    f.write(page_text)

