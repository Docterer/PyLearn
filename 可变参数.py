"""可变参数和不可变参数的学习"""
gl_num = 10

gl_list = [1, 3, 5]


# 使用到方法来赋值，会影响到全局变量的值
def modify(num):
    num = 3
    print("修改之后的num:%d" % num)


def modify_list(list):
    list.append(7)
    print("修改之后的list:", list)


def modify_plus_list(list):
    list += list
    print("相加之后的list:", list)


modify(gl_num)
print("gl_num=%d" % gl_num)
modify_list(gl_list)
print("gl_list:", gl_list)
modify_plus_list(gl_list)
print("gl_list 加等于：", gl_list)
