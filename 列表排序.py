"""列表排序"""
age_list = [1, 3, 5, 7, 9, 10, 8, 6, 4, 2]
age_list.sort()
print("自然排序", age_list)
age_list.sort(reverse=True)
print("降序", age_list)

name_list = ["刘能", "赵四", "王大拿", "长海"]
# 翻转
name_list.reverse()
print(name_list)

# 迭代遍历 iteration
for name in name_list:
    print(name)
