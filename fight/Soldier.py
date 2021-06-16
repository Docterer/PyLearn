from fight.Gun import Gun


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def __str__(self):
        return "战狼中队 [%s] 持枪[%s] 列队完毕" % (self.name, self.gun.model)

    def fire(self, gun):
        # 身份运算符，is 是判断两个标识符是不是引用的同一个对象 x==y 类似 id(x) == id(y)
        if self.gun is None:
            self.gun = gun
        self.gun.shoot()


gun = Gun("AK47", 10)
wolf = Soldier("吴京")
i = 0
while i < 12:
    i += 1
    wolf.fire(gun)
print(wolf)
