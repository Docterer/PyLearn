"""学习函数多个返回值"""


def measure():
    print("测量开始。。。")
    temp = 39
    wet = 50
    print("测量结果。。温度tmp = %d、湿度wet = %d" % (temp, wet))
    # 如果函数类型返回的是元祖，小括号可以省略
    # return (temp, wet)
    return temp, wet


print(measure())

num = 99


def test_send_param(num):
    num = 10


test_send_param(num)
print("num = %d" % num)
