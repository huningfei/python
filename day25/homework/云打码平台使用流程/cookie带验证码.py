import requests
from lxml import etree
import YunDaMa


# 该函数是用来使用云大码平台接口进行验证码识别，返回验证码对应的数据值
def getCode():
    # 普通用户用户名
    username = 'bobo328410948'

    # 密码
    password = 'bobo328410948'

    # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appid = 6003

    # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appkey = '1f4b564483ae5c907a1d34f8e2f2776c'

    # 图片文件
    filename = './code.png'

    # 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
    codetype = 2004

    # 超时时间，秒
    timeout = 5

    # 检查
    if (username == 'username'):
        print('请设置好相关参数再测试')
    else:
        # 初始化
        yundama = YunDaMa.YDMHttp(username, password, appid, appkey)

        # 登陆云打码
        uid = yundama.login();
        print('uid: %s' % uid)

        # 查询余额
        balance = yundama.balance();
        print('balance: %s' % balance)

        # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
        cid, result = yundama.decode(filename, codetype, timeout);
        print('cid: %s, result: %s' % (cid, result))

        return result


# 对带验证码的人人网登录页面进行请求发送，目的获取验证码图片
url = 'http://www.renren.com/SysHome.do'
headers = {
    # 对UA进行重写操作（伪装）
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
page_textBymainPage = requests.get(url=url, headers=headers).text
# 解析出验证码图片，下载到本地
tree = etree.HTML(page_textBymainPage)
codeImg_url = tree.xpath('//*[@id="verifyPic_login"]/@src')[0]
codeImg_data = requests.get(url=codeImg_url, headers=headers).content
with open('./code.png', 'wb') as fp:
    fp.write(codeImg_data)
    print('验证码下载成功')

# 进行登录操作，为了获取cookie
# 云打码流程：
# 注册普通和开发者用户
# 在开发者用户中下载示例代码 HTTPPython
# 在开发者用户中创建一个软件

# code = input('enter a code:')
code = getCode()
session = requests.session()
url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018901710806'
data = {
    'rkey': '2a442cd0c2f740407d5480c939cb9b50',
    'password': '2c195749c7255789411e985a029e806644a17c2bb5b475aa92c517502a1d7ee5',
    'origURL': 'http://www.renren.com/home',
    'key_id': '1',
    'icode': code,
    'f': '',
    'email': 'www.zhangbowudi@qq.com',
    'domain': 'renren.com',
    'captcha_type': 'web_login',
}
# 获取请求成功后的cookie数据（session）
session.post(url=url, data=data)

# 使用携带了cookie的session进行二级子页面的请求发送
url = 'http://www.renren.com/289676607/profile'
page_text = session.get(url=url, headers=headers).text
with open('./renren.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)