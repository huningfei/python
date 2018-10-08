from conf import settings
import os
import re

class Disk():
    def process(self,cmd_func,test):
        '''
        这是判断是测试模式还是正式环境
        :param cmd_func: 这是init文件里的初始化函数exec_cmd
        :param test: 判断是true还是false true是测试模式
        :return:
        '''
        if test:
            output = open(os.path.join(settings.BASEDIR, 'files/disk.out'), 'r', encoding='utf-8').read()
        else:
            output = cmd_func("sudo MegaCli  -PDList -aALL") # 如果是线上环境就执行cmd_func

        return self.parse(output)

    def parse(self, content):
        """
        解析shell命令返回结果
        :param content: shell 命令结果
        :return:解析后的结果
        """
        response = {}
        result = []
        for row_line in content.split("\n\n\n\n"):
            result.append(row_line)
        for item in result:
            temp_dict = {}
            for row in item.split('\n'):
                if not row.strip():
                    continue
                if len(row.split(':')) != 2:
                    continue
                key, value = row.split(':')
                name = self.mega_patter_match(key)
                if name:
                    if key == 'Raw Size':
                        raw_size = re.search('(\d+\.\d+)', value.strip())
                        if raw_size:

                            temp_dict[name] = raw_size.group()
                        else:
                            raw_size = '0'
                    else:
                        temp_dict[name] = value.strip()
            if temp_dict:
                response[temp_dict['slot']] = temp_dict
        return response

    @staticmethod
    def mega_patter_match(needle):
        grep_pattern = {'Slot': 'slot', 'Raw Size': 'capacity', 'Inquiry': 'model', 'PD Type': 'pd_type'}
        for key, value in grep_pattern.items():
            if needle.startswith(key):
                return value
        return False
