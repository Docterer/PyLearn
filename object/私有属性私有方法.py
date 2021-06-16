"""私有属性私有方法学习"""
class Secret:
    """
    私有方法和私有属性外界都不能访问。
    实际上，Python不存在严格意义上的私有属性私有方法。
    Python解释器在处理私有属性方法时会把方法名或者属性名 「__a」转成 『_类名__a』
    所以在外部可以通过 对象._类名__a访问到私有属性或方法
    """
    def __a(self):
        print("这是私有方法")
        self.__age = 18
        print("age是私有属性,值为%d" % self.__age)