"""全局变量的设置和修改"""
# 注意：在开发时，应该把模块中使用的全局变量都定义在所有函数上方
num = 10


def update_global():
    global num
    num = 20
    print("修改之后的num:%d" % num)


def update():
    num = 20
    print("这样修改全局变量num的值不会变 num=%d" % num)


update()
print("num 现在的值：%d" % num)
