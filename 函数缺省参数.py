"""函数缺省参数学习"""
# 缺省参数就是把函数常用的值当做默认值，这样就不需要传递参数

gl_list = [1, 2, 3, 4, 5, 6, 7]

# 默认升序
gl_list.sort()
# 降序
gl_list.sort(reverse=True)


# 指定函数的缺省参数
# 缺省参数定义的位置，必须在末尾
# 调用多个缺省参数的函数需要指定参数
def print_info(name, gender=False):
    """

    :param name: 姓名
    :param gender: True 男
    :return:
    """
    gender_text = "男"
    if not gender:
        print("不是男生")
        gender_text = "女"


print_info(name="小明", gender=True)
