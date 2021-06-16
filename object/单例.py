class YuanShou(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        # 判断类属性是否为空
        if cls.instance is None:
            # 调用父类方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 返回类属性保存的对象引用
        return cls.instance

    def __init__(self, name):
        self.name = name
        print("%s初始化" % name)


# 每次使用 类名() 创建对象时,python解释器都会自动调用两个方法
# 1.__new__() 分配空间
# 2.__init__() 对象初始化
y1 = YuanShou("mao")
y2 = YuanShou("xi")
print(y1)
print(y2)
print(y1 == y2)
print(y1.name)
print(y2.name)
