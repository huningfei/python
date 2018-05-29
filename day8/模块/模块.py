#import my_module as mm
money=2000
#mm.func()
#print(mm.money)
#总结
# 导入一个模块 就相当于执行了这个文件
# 一个模块如果执行多次import是什么效果？只执行一次

# from my_module import func as f ,money as m     #as就是重命名
# f()
# print(m)

# 模块总结
# 能不能导入模块 ： sys.path
# 导入模块的顺序 ： 内置 扩展 自定义
# 导入模块 ： 相当于执行了这个模块，文件中的名字会被存储在一块独立的内存空间中

# import
# 在全局创建了一个模块名，指向属于这个模块的命名空间
# 空间里存储了所有文件中的名字
# 起别名 import ... as ..
# 不推荐一行导入多个模块

# from import
# import后面的名字会出现在全局 ，相当于对独立命名空间中的一个引用
# from import 也支持 as语句 也支持 导入多个名字
# from import * 相当于导入所有名字,*和被导入模块__all__是互相影响的