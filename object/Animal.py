"""继承学习"""


class Animal:

    def __init__(self):
        print("初始化")

    def jump(self):
        print("jump")

    def run(self):
        print("Animal run")

    def __secret(self):
        print("私有方法")


class Homo:
    def __init__(self):
        print("尼安德特")

    def run(self):
        print("Homo run")

    def walk(self):
        print("bbq")


class Human(Animal, Homo):
    def run(self):
        # 子类方法中可以访问父类公有属性
        # super().run()
        # print("人跑得慢")
        # 子类方法中不能访问父类私有属性，不能调用私有方法
        # super()._Animal__secret()
        pass
    human_array = []

# 开发时尽量避免多继承
p = Human()
p.run()
p.walk()
p.human_array.append("a")
print(p.human_array)
print(dir(p))
# 子类不可以访问父类定义的私有方法,除非以下特殊方式，但是不建议使用
# p._Animal__secret()
