"""字符串切片"""

"""切片方法适用于 字符串，列表，元祖"""
"""
    切片使用索引值来限定范围，从一个大字符串中切出小的字符串
    切片无法使用在无序集合中
"""

num_str = "0123456789"

res1 = num_str[2:6]
print(res1)
res2 = num_str[:]
print(res2)
res3 = num_str[::-2]
print(res3)
res4 = num_str[::-1]
print(res4)
res5 = num_str[-1::-1]
print(res5)
