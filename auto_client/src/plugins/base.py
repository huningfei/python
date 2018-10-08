# 这是用的传参的方式
class Basic():
    def __init__(self):
        pass
    @classmethod
    def settings(cls):
        return cls()
    def process(self,cmd_func,test):
        '''
        这里获取的是最基本的系统信息
        :param cmd_func:
        :param test:
        :return:
        '''
        if test:
            output = {
                'os_platform': "linux",
                'os_version': "CentOS release 6.6 (Final)\nKernel \r on an \m",
                'hostname': 'c1.com'
            }
        else:
            output = {
                'os_platform': cmd_func("uname").strip(),
                'os_version': cmd_func("cat /etc/issue").strip().split('\n')[0],
                'hostname': cmd_func("hostname").strip(),
            }
        return output