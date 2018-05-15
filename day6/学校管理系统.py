#https://gitee.com/ygqygq2/python_homework/tree/master/day6%E4%BD%9C%E4%B8%9A
import pickle
import json
class School:
    def __init__(self,name,place):
        self.name=name
        self.place=place
    def create(self):
        dic={"name":self.name,"place":self.place}
        str=json.loads(dic)
        print(type(str))
        # with open('file',encoding='utf-8',mode='a') as f1:
        #     print(self.name)
        #     f1.write(str)



        #print('创建了%s校区，地址在%s'%(self.name,self.place))


    # def beijing(self):
    #     在北京-属性
    #
    # def shanghai(self):
    #     地点在上海-属性
beijing=School('北京','昌平沙河')
beijing.create()


# class 学员
#     选择学校-方法
#     选择班级-方法
#
#
#
# class 课程
#     linux方法 在北京开
#     周期和价格
#     go   方法 在上海开
#     周期和价格
#     python 方法 在北京开
#     周期和价格
# class 讲师
#     关联学校
#
# class 登录
#     学员登录-方法
#     讲师登录-方法
#     管理员登录-方法


