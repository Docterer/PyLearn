"""变量学习"""

num_value = 10


def demo1():
    # 局部变量
    # 定义一个局部变量，在函数内部使用，临时保存函数内部需要用到的数据
    # 局部变量的生命周期
    # 出生：执行了下方代码，变量才会被创建
    # 死亡：函数执行完成之后就死亡了
    num = 10
    print("num:%d" % num)
    print("num 内存地址 %d" % id(num))


def demo2():
    # 全局变量
    print("全局变量num_value内存地址：%d" % id(num_value))


demo1()
demo2()
