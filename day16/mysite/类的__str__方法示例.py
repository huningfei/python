class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        print("print 打印 某个具体对象时会自动调用执行的")
        return self.name


p = Person("alex", 9000)
print(p)
