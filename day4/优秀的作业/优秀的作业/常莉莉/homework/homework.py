#!/usr/bin/env python
#coding:utf-8

#Filename:  homework
#Author:    chang
#DATE:      2018-05-05 07:05
import re
import os

class staff():
	def __init__(self):
		pass
	def get_staff_info(self,file):
		if (os.path.exists(file))==False:
			print("查询的表不存在!")
			return
		else:

			with open (file,encoding="utf-8",mode="r") as f:
				content_row1=f.readline()
				title=content_row1.strip().split(",")
				lenth=len(title)
				staff_info=[]

				for i in f:
					staff_dic={}
					data = i.strip().split(",")
					for j in range(lenth):
						staff_dic.setdefault(title[j], data[j])

					staff_info.append(staff_dic)
			return staff_info

	def print_info(self,row_name,staff_temp):
		if row_name == '*':
			print(staff_temp)
		else:
			info = row_name.split(',')
			res = {}
			for i in info:
				#print (i)
				if i.strip() in staff_temp.keys():
					res.setdefault(i.strip(),staff_temp.get(i.strip()))
				else:
					print("查询的列不存在")
					return
			print(res)


	def logic_cal(self,staff_temp,logic_exp):
		logic_exp = re.search('(.+?)([=<>]{1,2}|like)(.+)',
		                      ''.join(logic_exp))  # 表达式列表优化成三个元素，形如[‘age','>=',20] 或 [‘dept','like','HR']

		if (logic_exp):
			logic_exp = list(logic_exp.group(1, 2, 3))

			if logic_exp[1]=="=":
				logic_exp[1]="=="

			if logic_exp[1] == 'like':  # 运算符为like的表达式运算
				return re.search(logic_exp[2].strip("'").strip('"'), staff_temp.get(logic_exp[0])) and True
			elif (logic_exp[0].isdigit() and logic_exp[2].isdigit()):  # 两头为数字的运算，直接eval函数转数学表达式
				return eval(''.join(logic_exp))
			elif (logic_exp[1] in ("==",">","<")):  # 非数字的运算，即字符串运算，此时逻辑符只可能是‘='，若用eval函数则字符串会转成无定义变量而无法计算，所以拿出来单独用"=="直接计算
				eval_list=[staff_temp.get(logic_exp[0]),logic_exp[1],logic_exp[2]]
				return(eval("".join(eval_list)))  # 字符串相等判别，同时消除指令中字符串引号的影响，即输引号会比记录中的字符串多一层引号
			else:  # 其他不合语法的条件格式输出直接返回False
				return False
		else:
			return False

	def verify(self,staff_temp, condition):
		if condition=='':
			return True
		condition_list = condition.split()

		if len(condition_list) == 0: return False
		logic_str = ['and', 'or', 'not']  # 逻辑运算字符串 且、或、非
		logic_exp = []  # 单个条件的逻辑表达式组成的列表，形如[‘age',' ','>','=',20] 或 [‘dept',' ','like',' ','HR']
		logic_list = []  # 每个条件的表达式的计算结果再重组后的列表，形如 [‘True','and','False','or','not','False']
		for i in condition_list:
			if i in logic_str:
				if (len(logic_exp) != 0):
					logic_list.append(str(self.logic_cal(staff_temp, logic_exp)))  # 逻辑表达式计算并将返回的True或False转化成字符串添加到列表
				logic_list.append(i)
				logic_exp = []
			else:
				logic_exp.append(i)
		logic_list.append(str(self.logic_cal(staff_temp, logic_exp)))
		return eval(' '.join(logic_list))  # 列表转化成数学表达式完成所有条件的综合逻辑运算，结果为True或False


	def select(self,command):
		command_phrase=re.findall(r"select(.*?)from(.*)",command)
		#print(command_phrase)
		if command_phrase:
			rows_name=command_phrase[0][0].strip()
			info=command_phrase[0][1].strip()
			if info.count("where ")>0:
				m=re.findall(r"(.*?)where(.*)",info)
				table_name=m[0][0].strip()
				condition=m[0][1].strip()
			else:
				table_name=info
				condition=""
			count = 0
			staff_list = []
			staff_temp=self.get_staff_info(table_name)
			if staff_temp:
				for i in staff_temp:
					if (self.verify(i, condition)):  # 验证员工信息是否符合条件
						count += 1
						staff_list.append(i)
				print("数据库本次共\033[31;1m查询到%d条\033[0m员工信息，如下:" % count)
				for staff_temp in staff_list:

					self.print_info(rows_name,staff_temp)  # 查询记录打印
		else:
			print("语法错误")


	def insert(self,command):
		pass
	def update(self,command):
		pass
	def delete(self,command):
		pass
	def func(self):
		func_dic={
			"select":self.select,
			"insert":self.insert,
			"update":self.update,
			"delete":self.delete,
		}
		while (True):
			command=input("请按照语法输入指令并以分号结束,退出请输入exit:").strip()
			func=func_dic.get(command.split(" ")[0], "error")
			if command.lower()=="exit":
				print("数据库操作结束")
				break
			elif func == "error":
				print("指令不存在,请重新输入!")
			else:
				func(command)










if __name__=="__main__":
	sf=staff()
	#print (sf.get_staff_info("staff"))
	sf.func()

