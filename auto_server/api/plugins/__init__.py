from django.conf import settings
from repository import models
import importlib
from .server import Server



class PluginManger(object):
    def __init__(self):
        self.plugin_items = settings.PLUGIN_ITEMS
        self.basic_key = "basic"
        self.board_key = "board"

    def exec(self,server_dict):
        '''

        :param server_dict: 客户端发送过来的数据
        :return:1,执行完全成功； 2, 局部失败；3，执行失败;4. 服务器不存在
        '''
        ret = {'code': 1, 'msg': None}
        hostname = server_dict[self.basic_key]['data']['hostname']
        server_obj = models.Server.objects.filter(hostname=hostname).first()
        if not server_obj:  # 如果没有这个主机，则返回ret,并不是去数据库直接创建主机了，你需要先去后台创建主机名才可以
            ret['code'] = 4
            return ret
        # 更新操作
        obj = Server(server_obj, server_dict[self.basic_key], server_dict[self.board_key])  # 执行server里面的函数，生成obj对象
        obj.process()
        # 对比更新[硬盘，网卡，内存，可插拔的插件]
        for k, v in self.plugin_items.items():  # 去循环setting里面的配置的硬盘，内存信息
            # "nic": "api.plugins.nic.Nic",
            try:
                module_path, cls_name = v.rsplit('.', maxsplit=1)
                md = importlib.import_module(module_path)
                cls = getattr(md, cls_name)
                # cls是指disk，nic,memory等插件
                obj = cls(server_obj, server_dict[k])  # server_obj是主机名，server_dict[k]是指硬盘或者内存的数据
                # print(obj)

                obj.process()
            except Exception as e:
                ret['code'] = 2
        return ret
