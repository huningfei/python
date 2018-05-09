import re


ret = re.findall('a','abc egon yuan') # 返回所有满足匹配条件的结果,放在列表里
print(ret) ##结果['a', 'a']

ret1 = re.search('\d+','8787abc 97897engo yuan657').group()#函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以
# 通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。
print(ret1) ##结果 8787  只匹配第一个数字

ret3=re.match('\d+','1abc78797 97897engo yuan657').group()# 同search,不过只能在字符串开始处进行匹配
print(ret3)
# #ret4=re.match('a','bca').group()  ##这种的就会报错
# # print(ret4)
ret5=re.split('[ab]','abcd')#先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割
print(ret5) ##结果['', '', 'cd']
ret6 = re.sub('\d', 'H', 'eva3egon4yuan4', 1)##将数字替换成'H'，参数1表示只替换1个
print(ret6)
ret7 = re.subn('\d', 'H', 'eva3egon4yuan4')#将数字替换成'H'，返回元组(替换的结果,替换了多少次)
print(ret7)

obj = re.compile('\d{3}')  #将正则表达式编译成为一个 正则表达式对象，规则要匹配的是3个数字
ret8 = obj.search('abc123eeee') #正则表达式对象调用search，参数为待匹配的字符串
print(ret8.group())

ret = re.finditer('\d', 'ds3sy4784a')
print(ret)
print(ret.__next__().group())
print(next(ret).group())

#第二种取值方式
print([i.group()for i in ret])


##findall优先级
ret = re.findall('www\.(oldboy|baidu)\.com', 'www.oldboy.com')
##这是因为findall会优先把匹配结果组里内容返回,如果想要匹配结果取消优先级
print(ret)##结果是oldboy

ret = re.findall('www\.(?:baidu|oldboy)\.com', 'www.oldboy.com')
print(ret)  # ['www.oldboy.com']

##split优先级查询
ret = re.split("\d+",'eva3egon4yuan')
print(ret)

ret = re.split('(\d+)','eva3egon4yuan')
print(ret)

##在匹配部分加上（）之后所切出的结果是不同的，
#没有（）的没有保留所匹配的项，但是有（）的却能够保留了匹配的项，
#这个在某些需要保留匹配部分的使用过程是非常重要的