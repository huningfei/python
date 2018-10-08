import os
import importlib
from . import global_settings

class Settings(object):
    # 这个类是用来获取两个配置文件里面的信息的
    # global_settings, 全局配置获取
    # settings.py，默认配置获取
    def __init__(self):
        # 这个是获取全局变量里面的值
        for item in dir(global_settings):   # dir可以查看global_settings里面所有的变量
            if item.isupper(): #如果是大写，才往下执行，item就是k，
                k = item
                v = getattr(global_settings,item) # 根据字符串去里面找value
                setattr(self,k,v) # self是个对象，就相当于self.test=true
        # 默认
        setting_path = os.environ.get('AUTO_CLIENT_SETTINGS')
        md_settings = importlib.import_module(setting_path)
        for item in dir(md_settings):
            if item.isupper():
                k = item
                v = getattr(md_settings, item)
                setattr(self, k, v)

settings=Settings()