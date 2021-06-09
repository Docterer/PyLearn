"""多值参数学习"""
"""
    定义支持多值参数的函数
    参数名前增加一个 * 可以接受元祖
    参数名前增加两个 ** 可以接受字典
"""

"""
    开发习惯
    *args---------存放元祖
    **kwargs------存放字典
"""


def demo(name, *args, **kwargs):
    print(*args)
    print(**kwargs)


demo("wo", (1,), {"gui": "sb"})


def plus(*args):
    res_sum = 0
    for arg in args:
        res_sum += arg
    print("累加值=%d" % res_sum)


plus(1, 2, 3, 4, 5, 6, 7)
