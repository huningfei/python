from selenium import webdriver
import time

# 创建一个浏览器
bro = webdriver.Chrome(executable_path=r'./chromedriver_win32/chromedriver.exe')  # 取得程序的路径

# 打开浏览器
url = 'https://www.baidu.com'
# 发送请求
bro.get(url=url)
time.sleep(3)

# 调用seleniem提供的接口
# 找到指定的搜索框
myInput = bro.find_element_by_id("kw")
# 在对应搜索框录入指定的词条
myInput.send_keys('美女')
time.sleep(2)

# 点击搜索，定位到搜索按钮
myButton = bro.find_element_by_id('su')

myButton.click()  # 点击按钮
time.sleep(2)
# myButton2=bro.find_elements_by_xpath('//*[@id="3"]/h3/a')[0].click()


# 关闭浏览器
bro.quit()
