"""递归的学习"""


# 累加器
def sum_number(num):
    # 必须设置递归的出口
    if num == 1:
        return 1
    temp = sum_number(num - 1)
    res = temp + num
    return res


# 默认递归次数是有限的
print(sum_number(100))
