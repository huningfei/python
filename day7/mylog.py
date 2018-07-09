# logging
# 日志
# 程序出错 -- 日志 对内看的
# 给用户看的 对外看的
import logging
# 简单配置
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='test.log',
#                     filemode='w'
#                     )
# logging.debug('debug message')    # 非常细节的日志 —— 排查错误的时候使用
# logging.info('info message')     # 正常的日志信息
# logging.warning('warning message')  # 警告
# logging.error('error message')    # 错误
# logging.critical('critical message') # 严重错误

# logger对象的方式配置

# 吸星大法

def mylog():
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
    # logger.debug('logger debug message')
    # logger.info('logger info message')
    # logger.warning('logger warning message')
    # logger.error('程序出错了')
    # logger.critical('logger critical message')
mylog()