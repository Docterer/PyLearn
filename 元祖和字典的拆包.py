"""元祖和字典的拆包"""

gl_nums = (1, 2, 3, 4, 5, 6, 7)
gl_dict = {"name": "ming", "age": 18}


def demo(*args, **kwargs):
    print(args)
    print(kwargs)


demo(*gl_nums, **gl_dict)
