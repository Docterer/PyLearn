"""元祖学习"""
# 元祖中保存的数据类型通常不一样
data_tuple = ("你", "好", 1)
print(type(data_tuple))
count = data_tuple.count("你")
print(count)
print(data_tuple.index("你"))

""" 格式化字符串后面的'()'本质上是元祖 """
print("统计 %d, 你在元祖中的下标：%d" % (count, data_tuple.index("你")))
# print("元祖第一个值:%s，元祖第二个值:%s" % data_tuple)

data_list = list(data_tuple)
print(data_list)

