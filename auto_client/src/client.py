from src.plugins import PluginManager
from conf import settings
import requests
from concurrent.futures import ThreadPoolExecutor  # 导入线程模块


class BaseClient(object):  # 公共类，都向服务端发送数据
    def __init__(self):
        self.api = settings.API

    def post_server_info(self, server_dict):
        '''
        向服务端发送收集好的信息
        :param server_dict: 这是从客户端上面收集到的信息
        :return:
        '''
        # requests.post(self.api, data=server_dict)  # 通过from表单提交的k=v&k=a用这种方式发送，服务端只能收到key,不能获取value
        response = requests.post(self.api, json=server_dict)  # 1 字典序列化，2 带请求头 content-type；application/json
        print(response)

    def exec(self):
        raise NotImplementedError("必须实现exec方法")


class AgentClient(BaseClient):  # agent方式
    def exec(self):
        obj = PluginManager()
        server_dict = obj.exec_plugin()
        print('采集到服务器信息', server_dict)
        self.post_server_info(server_dict)  # 调用post_server_info向服务端发送数据


class SaltSshClient(BaseClient):  # Salt和ssh模式写到一起
    def get_host_list(self):
        return ['c1.com', 'c2.com']  # 返回一个主机列表

    def task(self, host):
        obj = PluginManager(host)  # 实例化一个对象
        server_dict = obj.exec_plugin()
        print(server_dict)
        self.post_server_info(server_dict)

    def exec(self):
        pool = ThreadPoolExecutor(10)  # 开启10个线程,每次处理10个
        host_list = self.get_host_list()
        for host in host_list:
            pool.submit(self.task, host)  # 异步提交任务和参数
