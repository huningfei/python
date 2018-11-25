#需求，去批量下载梨视频
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
import re

# 创建一个无头谷歌浏览器

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# 驱动路径
path = r'D:\python21\python\day26\selenium自动化操作\chromedriver_win32\chromedriver.exe'

# 创建浏览器对象
browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)

# 浏览器打开url
browser.get(url="http://www.pearvideo.com/category_59")

# 让滚轮向下滑动，加载更多的数据执行js
js = "window.scrollTo(0,document.body.scrollHeight)"

browser.execute_script(js)

# 获取页面圆满数据，进行解析
page_text = browser.page_source  # page_source可以获得当前浏览器对应的页面数据，不需要用request

# 使用xpath去进行解析操作
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="categoryList"]/li')
# print(li_list)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

for li in li_list:
    secondPage_url = "http://www.pearvideo.com/" + li.xpath('./div/a/@href')[0]
    # 对上述url发起请求，获取二级页面的页面数据
    page_text = requests.get(url=secondPage_url, headers=headers).text
    video_url = re.findall('srcUrl="(.*?)",', page_text, re.S)[0] #使用正则去匹配url
    videoData = requests.get(url=video_url, headers=headers).content
    fileName = video_url.split('/')[-1]
    with open(fileName, 'wb') as fp:
        fp.write(videoData)
        print(fileName + '已经被下载完毕')
