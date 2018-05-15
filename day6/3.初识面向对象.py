# 函数 基础数据类型 循环 文件处理 模块
# 游戏公司
# 人狗大战
# 两个角色
# 人
    # 昵称
    # 性别
    # 生命值
    # 战斗力
    # 背包
# 狗
    # 昵称
    # 品种
    # 生命值
    # 战斗力
def Person(name,sex,hp,dps):   # 人模子
    dic = {'name':name,'sex':sex,'hp':hp,'dps':dps,'bag':[]}
    def attack(dog):
        dog['hp'] -= dic['dps']
        print('%s打了%s,%s掉了%s点血,剩余%s点血' % (dic['name'], dog['name'], dog['name'], dic['dps'], dog['hp']))
    dic['attack'] = attack
    return dic
def Dog(name,kind,hp,dps):   # 狗模子
    dic = {'name':name,'kind':kind,'hp':hp,'dps':dps}
    def bite(person):
        person['hp'] -= dic['dps']
        print('%s咬了%s,%s掉了%s点血,剩余%s点血' % (dic['name'], person['name'], person['name'], dic['dps'], person['hp']))
    dic['bite'] = bite
    return dic
alex = Person('alex','不详',250,5)
ha2 = Dog('哈士奇','藏獒',15000,200)
# 人打狗
print(alex)
print(ha2)
print(alex['attack'])
alex['attack'](ha2)
print(ha2)


# 面向对象的编程思想
# 人狗大战
# 创建一个人
# 创建一个狗
# 人打狗 —— 函数
# 狗咬人 —— 函数

# 造模子 —— 面向对象
# 规范了一类角色的属性项目、属性的名字、技能、技能的名字
# 权限 有一些函数 只能是这个角色才能拥有 才能调用