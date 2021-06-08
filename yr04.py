"""石头剪刀布"""
import random

compute = random.randint(1, 3)

player = int(input("请输入要出的拳 石头（1）/ 剪刀（2）/ 布（3）:"))

if (player == 3 and compute == 1) or (player == 1 and compute == 2) or (player == 2 and compute == 3):
    print("玩家赢")
elif player == compute:
    print("平手")
else:
    print("电脑赢")

"""循环语句"""
b = 0
res = 0
while b < 100:
    b += 1
    # res += b
    if b % 2 == 0:
        continue
        res += b
print("res: %d" % res)


