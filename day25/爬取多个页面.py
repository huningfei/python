import requests
import ssl

# 需求：爬取搜狗知乎指定词条指定页码下的页面数据
headers = {
    # 对UA进行重写操作（伪装）
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}



url = 'http://zhihu.sogou.com/zhihu?'
word = input('enter a word:')

start_page = int(input('enter a start page:'))
end_page = int(input('enter a end page:'))
for page in range(start_page, end_page + 1):
    param = {
        'query': word,
        'page': str(page)  # 请求携带的参数必须为str
    }
    response = requests.get(url=url, params=param, headers=headers, proxies={"https": '183.111.235.198:8080'})

    print(response.url)
    page_text = response.text
    file_name = word + str(page) + ".html"  # 文件名字为word+数字
    with open(file_name, 'w', encoding='utf-8') as fp:
        print('爬去到了第%d页的页面数据' % page)
        fp.write(page_text)
