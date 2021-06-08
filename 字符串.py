"""字符串学习"""
self_str = "我爱天天洗澡，天天洗澡身体好好"

for c in self_str:
    print(c)

print("字符串长度：%d" % len(self_str))

# 统计次数
print("%s 出现的次数 : %d" % ("天", self_str.count("天")))

# 出现位置
print("%s 第一次出现的位置 : %d" % ("天", self_str.index("天")))

str_list = self_str.split("\n")
print(str_list)
print(self_str.islower())

# 判断是否以指定的字符串开始
res = self_str.startswith("我")
print(res)

# 判断是否以指定字符串结束
res2 = self_str.endswith("我")
print(res2)

# 查找指定字符串
# res3 = self_str.index("门")
res4 = self_str.find("贵")
# find方法 如果指定字符串不存在返回「-1」，index则会报错
# print("指定字符串出现的位置%d" % res3)
print("指定字符串出现的位置%d" % res4)

# 替换字符串
new_str = self_str.replace("天天", "日日")
print(self_str)
print(new_str)

poem = ["登鹳雀楼", "白日依 山尽", "黄河 入海流", "欲穷千里目", "更上一层楼"]
for poem_str in poem:
    # print("|%s|" % poem_str.center(20, " "))
    # print("|%s|" % poem_str.ljust(20, " "))
    # print("|%s|" % poem_str.rjust(20, " "))
    print("%s" % poem_str.strip())

str1 = "你好"
str2 = "好的"
str3 = str1+str2
str4 = str1.join(poem)
print(str4)
