"""类属性学习"""


class Tool(object):
    # 对象属性
    count = 0

    def __init__(self, name):
        # 实例属性
        self.name = name

        Tool.count += 1


t1 = Tool("刀")
t2 = Tool("斧子")
print(Tool.count)
