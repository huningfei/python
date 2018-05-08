##collections模块
import collections
#orderedDict 有序字典
# d = collections.OrderedDict()
#
# d['苹果'] = 10
# d['手机']=5000
# print(d)
# for i in d:
#     print(i,d[i])


##defaultdict 默认字典
##小于66的放到k2，大于66的放到k1,形成一个新字典
from collections import defaultdict
#l= [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
##常规写法
# new_dict={}
# for value in l:
#     if value>66:
#         if new_dict.has_key('k1'):
#             new_dict['k1'].append(value)
#         else:
#             new_dict['k1']=value
#     else:
#         if new_dict.has_key('k2'):
#             new_dict['k2'].append(value)
#         else:
#             new_dict['k2'] = value
# print(new_dict)


##默认字典写法
# new_dict = defaultdict(list)
# for value in l:
#     if value > 66:
#         new_dict['k1'].append(value)
#     else:
#         new_dict['k2'].append(value)
# print(new_dict)

##namedtuple 生成可以使用名字来访问元素内容的tuple
# from collections import namedtuple
# Point = namedtuple('point',['x','y'])
# p=Point(1,2)
# print(p.x)
# print(p.y)

#deque双端队列
# from collections import deque
# q=deque()
# print(q)
# q.append(1)
# q.append(2)
# print(q)
# q.pop()
# print(q)
# q.appendleft('a')
# q.appendleft('b')
# print(q)
# q.popleft()
# print(q)

##time时间模块
import time
# print(time.time()) ##时间戳时间
# print(time.strftime('%Y-%m-%d %H:%M:%S'))##字符串时间
# print(time.localtime()) ##结构化时间
##时间转换
# print(time.localtime(1600000000)) ##时间戳转换成结构化时间
# struct_time=time.gmtime(1600000000)
# print(time.strftime('%Y-%m-%d %H:%M:%S',struct_time))##结构化转换成字符串

##字符串时间转换成时间戳时间
# s = '2015-12-3 8:30:20'
# ret = time.strptime(s,'%Y-%m-%d %H:%M:%S')  ##字符串转换成结构化
# print(ret)
# print(time.mktime(ret)) ##结构化转换成时间戳


'''
##计算两个时间段相隔了多长时间
#第一种写法
true_time=time.mktime(time.strptime('2008-05-12 08:30:00','%Y-%m-%d %H:%M:%S'))
time_now=time.mktime(time.strptime('2018-05-07 11:00:00','%Y-%m-%d %H:%M:%S'))
dif_time=time_now-true_time  ##得到是一个时间戳
ret=time.gmtime(dif_time) ##把时间戳转换成结构化时间
print(ret)
print('过去了%d年%d月%d天%d小时%d分钟%d秒'
%(ret.tm_year-1970,ret.tm_mon-1,ret.tm_mday-1,ret.tm_hour,ret.tm_min,ret.tm_sec))
'''

'''
##第二种写法 计算现在的时间跟1991年相差了多少时间
ago_time='1991-1-3'
now_time=time.localtime()
current_time=time.strptime(ago_time,'%Y-%m-%d')
# print(now_time)
# print(current_time)
#cha_time=now_time-current_time
print('过去了%d年%d月%d天'
%(now_time.tm_year-current_time.tm_year,now_time.tm_mon-current_time.tm_mon,now_time.tm_mday-current_time.tm_mday))
'''

##random 模块可以用于随机生成可用于验证码
import random
# print(random.random()) ##是介于0和1之间的小数
# print(random.uniform(1,4)) ##介于1和4之间的的小数
# print(random.randint(1,5)) ##介于1和5之间的随机整数
##随机生成一个四位的验证码
# s=''
# for i in range(4):
#     s+=str(random.randint(0,9))
# print(s)

'''
##随机生成一个字母和数字组合的验证码
#(65,90)A-Z  (97,122)a-z
import random
yanzheng=''
for i in range(6):
    num1=random.randint(65,90)
    alpha1=chr(num1)
    num2=random.randint(97,122)
    alpha2=chr(num2)
    num3=str(random.randint(0,9))
    #print(alpha1,alpha2,num3)
    s=random.choice([alpha1,alpha2,num3])
    yanzheng+=s
print(yanzheng)
'''


#sys模块 python解释器
import sys
#sys.exit() ##解释器退出，程序结束
# print(sys.path) #一个模块是否能够被导入 全看在不在sys.path列表所包含的路径下
# print(sys.modules) ## 放了所有在解释器运行的过程中导入的模块名
# print(sys.argv)
##注意，不能在pyhon里面直接执行，应该是D:\python21\day5\模块.py这种执行方式
'''
if sys.argv[1]=='hu' and sys.argv[2]=='123':
    print('登录成功')
else:
    sys.exit()
'''


##os模块
import os
# print(os.getcwdb())#获取当前目录
# os.chdir('C:\python21') #更改目录
# print(os.getcwdb())
#
# ret = 'path1%spath2'%os.pathsep  #输出用于分割文件路径的字符串 win下为;,Linux下为:
# print(ret)

print(os.name) #输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
#print(os.makedirs(r'c:/a/b')) ##创建多级目录
#os.removedirs(r'c:/a/b')# 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
#print(os.listdir(r'c:\python21')) ##列出当前目录所有的文件和目录，以列表形式打印
# print(os.environ) ##获取系统环境变量

#os.system("dir")  ##运行shell命令，直接显示，不用打印
# ret = os.popen("dir").read() ##运行shell命令，获取执行结果,需要打印
# print(ret)
##os.path
# print(os.path.abspath(r'模块.py')) ##获取绝对路径
# #结果C:\python21\day5\模块.py
# print(os.path.dirname('C:\python21\day5\模块.py')) ##获取上一级目录
# #结果C:\python21\day5
# print(os.path.split('C:\python21\day5\模块.py'))#将path分割成目录和文件名二元组返回
# #结果('C:\\python21\\day5', '模块.py')
# print(os.path.basename('C:\python21\day5\模块.py')) ##只获取到文件名
#结果：模块.py
# print(os.path.exists('C:\python21\day5\模块.py'))##判断路径是否存在，存在返回true
# print(os.path.isabs(r'模块.py')) ##判断是否是绝对路径，是返回true
# print(os.path.isfile('C:\python21\day5'))  ##判断是否是文件，是返回true
# print(os.path.isdir('C:\python21\day5')) ##判断是否是目录，是返回true
# print(os.path.join('c:','python21'))##将多个路径组合后返回
# print(os.path.getatime('C:\python21\day5')) #获取文件目录最后访问时间
# print(os.path.getmtime('C:\python21\day5')) #获取文件目录最后修改时间
# print(os.path.getsize(r'C:\python21\day5\模块.py'))#获取文件大小
# print(os.path.getsize(r'C:\python21\day4'))#获取目录大小
##获取目录下文件大小  ##计算不在同一目录下的文件大小
# dirs = "C:\python21\day4"
# sum=0
# C:\python21\day4\ceshi.py
# for path in ret:
#     if os.path.isfile(os.path.join(dirs, path)):
#         sum+=os.path.getsize(os.path.join(dirs,path))
# print(sum)

##同一目录下文件的大小
# ret = os.listdir(r'C:\python21\day5')
# for path in ret:
#     if os.path.isfile(path):
#         sum+=os.path.getsize(path)
# print(sum)

##计算文件夹下面的文件及其文件夹下的文件夹

'''
sum=0

def func(dirs):  # 'C:\python21\day5') ##默认是字符串
    global sum
    for file in os.listdir(dirs):##列出dirs目录下面所有的文件及其目录
        if os.path.isdir(os.path.join(dirs,file)): ##
            
            # dirs 是 C:\python21\day5\a
            # file是 目录下面的文件 C:\python21\day5\a\b.txt
            
            func(os.path.join(dirs,file))
        else:
            print("%s:%s" % (file,os.path.getsize(os.path.join(dirs,file))))
            sum+=os.path.getsize(os.path.join(dirs,file))
    return sum
print(func(r'C:\python21\day5'))
'''
#
###打印列表里面的每个元素，直到没有列表为止
# lst=[1,[2,[3,[4]]],"a"]
# def func(lst):
#     for i in lst:
#         if type(i) == list:
#             func(i)
#         else:
#             print(i)
# func(lst)

sum = 0
def func(dirs):
    global sum

    for file in os.listdir(dirs):
        if os.path.isdir(os.path.join(dirs,file)):
            func(os.path.join(dirs,file))
        else:
            sum+=os.path.getsize(os.path.join(dirs,file))
            print("%s:%s" % (file,os.path.getsize(os.path.join(dirs,file))))
    return sum
print(func(r'C:\python21\day4'))

