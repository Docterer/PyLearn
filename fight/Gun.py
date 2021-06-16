class Gun:
    def __init__(self, model, bullet_count):
        self.model = model
        self.bullet_count = bullet_count
        self.bullet_last = bullet_count

    def add_bullet(self, bullet_add_count):
        """
        添加子弹
        :param bullet_add_count:子弹添加数量
        :return:
        """
        if bullet_add_count + self.bullet_last > self.bullet_count:
            self.bullet_last = self.bullet_count
            print("添加进去 %d 颗子弹" % bullet_add_count + self.bullet_last - self.bullet_count)
            return
        if bullet_add_count + self.bullet_last <= self.bullet_count:
            self.bullet_last = bullet_add_count + self.bullet_last
            print("添加进去 %d 颗子弹" % bullet_add_count)

    def shoot(self):
        if self.bullet_last <= 0:
            print("没有子弹了，请装填...")
            return
        self.bullet_last -= 1
        print("==>")
        print("剩余子弹【%d】颗，射得好爽" % self.bullet_last)
