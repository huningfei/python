import logging
# from conf import setting

def mylog():
    logger = logging.getLogger()
    # 吸星大法

    # 先创造一个格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # 往文件中输入
    fh = logging.FileHandler('./logs/info.log', encoding='utf-8')  # 创造了一个能操作文件的对象fh
    fh.setFormatter(formatter)  # 高可定制化
    logger.addHandler(fh)
    logger.setLevel(logging.DEBUG)
    # fh.setLevel(logging.INFO)  # 文件里面显示error级别以上的
    return logger