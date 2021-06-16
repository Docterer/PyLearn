class ClassMethod(object):

    # 类属性
    count = 0

    @classmethod
    def a1(cls):
        print("类方法")
        print("类属性 %s的值为%d" % (cls.__name__, cls.count))

    @staticmethod
    def a2():
        print("静态方法")


class ClassMethodExtend(ClassMethod):

    def a1(self):
        print("hh")
        super().a1()


c1 = ClassMethodExtend()
c1.a1()