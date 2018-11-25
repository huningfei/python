# 必须先登录，然后去浏览器里面--network---找到登录页面--login--headers,查看参数在formdata里面

# Doubai123
import requests

url = 'https://accounts.douban.com/login'
# post请求携带参数设置
data = {
    'source': 'movie',
    'redir': 'https://movie.douban.com/',  # 登录成功之后跳转的页面
    'form_email': 'huningfei@126.com',
    'form_password': 'Doubai123',
    'login': '登录',
}
# 自定义hearders
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
# 请求
response = requests.post(url=url, data=data,headers=headers)

# 获取响应数据
page_text = response.text

# 持久化存储
with open('./doubai.html', 'w', encoding='utf-8') as f:
    f.write(page_text)
