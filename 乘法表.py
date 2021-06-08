"""九九乘法表"""
def multiple_data():
    a = 1
    b = 1
    res = 1
    while a <= 9:
        while b <= a:
            res = a * b
            b += 1
            print("%d=%d*%d" % (res, a, b), end="\t")
        print("")
        a += 1
        b = 1
    print("\'")