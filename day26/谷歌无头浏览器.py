from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import time
# 创建一个参数对象，用来控制谷歌浏览器无界面打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# 驱动路径
path=r'D:\python21\python\day26\selenium自动化操作\chromedriver_win32\chromedriver.exe'
#创建浏览器对象
browser=webdriver.Chrome(executable_path=path,chrome_options=chrome_options)
# 上网
url='http://www.baidu.com/'
browser.get(url=url)
time.sleep(2)
browser.save_screenshot('baidu.png') #后缀推荐用png,jpg会提示信息
browser.quit()

