import sys
import os
import importlib  # 可以导入字符串模块

os.environ['AUTO_CLIENT_SETTINGS'] = "conf.settings"  # 设置环境变量

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
# from src.plugins import func # 函数版
# from src.plugins import PluginManager  # 类版
from src import script

if __name__ == '__main__':
    script.start()
    # obj = PluginManager()  # 实例化一个对象
    # server_dict = obj.exec_plugin()  # 执行PluginManager类里面的一个exec_plugin方法
    # print(server_dict)
