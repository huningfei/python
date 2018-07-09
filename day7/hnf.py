import logging
def mylog():
    global sh
    logger = logging.getLogger()
    # 先创造一个格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # 往文件中输入
    fh = logging.FileHandler('log.log',encoding='utf-8')   # 创造了一个能操作文件的对象fh
    fh.setFormatter(formatter) # 高可定制化
    logger.addHandler(fh)
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler() #sh是在屏幕上面显示的
    # sh.setFormatter(formatter1)
    logger.addHandler(sh)
    fh.setLevel(logging.ERROR) #文件里面显示error级别以上的
    sh.setLevel(logging.DEBUG)  #屏幕上面显示debug级别以上的
    return logger
mylog()

def func():
    print('ok')


name=input('name:')
pwd=input('pwd:')
if name =='hu' and pwd =='123':
    #ret=mylog()

    sh.setLevel(logging.info('登录成功'))
    print('登录成功')
    func()
else:
    print('登录失败')

