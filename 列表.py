"""列表学习"""
user_list = ["a", "b", "c"]
a = user_list[0]
print(a)
"""拼接元素"""
user_list.append("d")
# 指定下标位置插入元素
user_list.insert(2, "e")
try:
    """获取下标"""
    b = user_list.index("d")
except:
    print("报错")
print(user_list)

user_list2 = ["刘能", "赵四", "王大拿", "长海"]
"""list 拼接 list"""
user_list.extend(user_list2)

# 移除指定元素（会删除列表中出现的第一个数据），数据不存在，程序报错
user_list.remove("王大拿")
print(user_list)
# 移除最后的元素
user_list.pop()
print(user_list)
# 指定删除元素的索引
user_list.pop(0)
print(user_list)
# 列表长度
user_list_len = len(user_list)
print("列表长度:%d" % user_list_len)

# count 统计列表中某个数据出现的次数
user_list.append("王大拿")
count = user_list.count("王大拿")
print("出现的次数：%d" % count)


# 使用del 关键字删除列表元素 delete 会把变量从内存中删除
del user_list[0]
print(user_list)
# 清空列表
user_list.clear()
print(user_list)
