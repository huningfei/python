# import glance.api.policy as hnf
# hnf.get()
#
# import glance.api.policy
# glance.api.policy.get()
#
# from glance.api import policy
# policy.get()
#导入一个文件相当于执行了这个文件中的代码
#导入一个包相当于执行这个包中的init文件
#import 后面的这个名字，永远会出现在全局的命名空间里

import glance  #绝对导入，其余的在init文件里面实现
#在glace里面的init文件里写的：from glance import api
#在api里面的init文件里写的：from glance.api import policy
glance.api.policy.get()

#相对导入
import glance
#在glace里面的init文件里写的：from . import api
#在api里面的init文件里写的：from .import policy
glance.api.policy.get()


