class Person:

    # 对象生命周期
    # 1.一个对象从调用 类名()创建，生命周期开始
    # 2.一个对象的__del__方法一旦被调用，生命周期结束
    # 3.在对象生命周期内，可以访问对象属性，或者让对象调用方法

    # 初始化方法，定义一个类具有哪些属性和方法
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        print("初始化")

    # 当对象销毁前，自动调用delete
    def __del__(self):
        print("我走了")

    # 自定义对象打印信息
    def __str__(self):
        return "我是[%s]，体重%.2f公斤" % (self.name, self.weight)

    def drink(self):
        print("%s 喝" % self.name)

    def eat(self):
        print("大吃一顿")
        self.weight += 10


# 创建对象
bb = Person("鬼佬", 100.0)
bb.eat()
print(bb)
# del ming
