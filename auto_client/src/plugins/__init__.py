from lib.config import settings  # 全局的配置文件
import importlib
from conf import settings  # 用户配置的配置文件
import requests
import traceback  # 获取详细的报错信息


# def func():
#     '''
#     函数版
#     :return:
#     '''
#     server_info = {}
#     # 高度可扩展，可插拔式插件，参考Django源码中的中间件。
#     for k, v in settings.PLUGIN_ITEMS.items():
#         # 找到v字符串：src.plugins.nic.Nic，src.plugins.disk.Disk
#         module_path, cls_name = v.rsplit('.', maxsplit=1)  # 以点为分隔符，从右边第一个点开始
#         module = importlib.import_module(module_path)  # 模块名字<module 'src.plugins.disk'
#         print(module)
#         cls = getattr(module, cls_name)  # 类名src.plugins.disk.Disk'
#         print(cls)
#         obj = cls()
#         ret = obj.process()  # 接收函数返回来的值
#         server_info[k] = ret  # 把k和接收的值存放到字典里面，k是键值

# 类封装版
class PluginManager():
    def __init__(self, hostname=None):
        self.hostname = hostname
        self.plugin_items = settings.PLUGIN_ITEMS  # 插件列表
        self.mode = settings.MODE  # 收集模式
        self.test = settings.TEST
        if self.mode == "SSH":
            self.ssh_user = settings.USERNAME
            self.ssh_port = settings.PORT
            self.ssh_pwd = settings.PASSWORD

    def exec_plugin(self):
        '''
        收集插件信息的比如，内存，硬盘，运行每个插件里面的命令
        :return:
        '''
        server_info = {}
        # 高度可扩展，可插拔式插件，参考Django源码中的中间件。
        for k, v in settings.PLUGIN_ITEMS.items(): # 去settings配置文件里面循环
            info = {'status': True, 'data': None, 'msg': None}  # 分别是状态，数据，报错信息
            try:
                # 找到v字符串：src.plugins.nic.Nic，src.plugins.disk.Disk
                module_path, cls_name = v.rsplit('.', maxsplit=1)  # 以点为分隔符，从右边第一个点开始
                module = importlib.import_module(module_path)  # 模块名字<module 'src.plugins.disk'
                # print(module)
                cls = getattr(module, cls_name)  # 类名src.plugins.disk.Disk'
                # print(cls)
                if hasattr(cls, 'initial'):
                    obj = cls.initial()  # 用的静态方法
                else:
                    obj = cls()  # 实例化一个对象 obj就是每个插件里面的类名，如Disk

                ret = obj.process(self.exec_cmd, self.test)  # 去执行类里面的process方法并接收函数返回来的值

                #ret结构：{'eth0': {'up': True, 'hwaddr': '00:1c:42:a5:57:7a', 'ipaddrs': '10.211.55.4', 'netmask': '255.255.255.0'}}
                info['data'] = ret
            except Exception as e:
                info['status'] = False
                info['msg'] = traceback.format_exc()
            server_info[k] = info  # 把k和接收的值存放到字典里面，k是键值比如nic,memory
        return server_info

    def exec_cmd(self, cmd):
        '''
        判断使用哪种模式
        :param cmd:用户传入的命令
        :return:
        '''
        if self.mode == "AGENT":
            import subprocess
            result = subprocess.getoutput(cmd)
        elif self.mode == "SSH":
            import paramiko
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=self.hostname, port=self.ssh_port, username=self.ssh_user, password=self.ssh_pwd)
            stdin, stdout, stderr = ssh.exec_command(cmd)
            result = stdout.read()
            ssh.close()
        elif self.mode == "SALT":
            import subprocess
            result = subprocess.getoutput('salt "%s" cmd.run "%s"' % (self.hostname, cmd))
        else:
            raise Exception("模式选择错误：AGENT,SSH,SALT")
        return result
