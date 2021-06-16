class Game(object):
    score = 0

    def __init__(self, name):
        self.name = name

    @staticmethod
    def show_help():
        print("帮助手册")

    @classmethod
    def show_top_score(cls):
        print("历史记录 %d" % cls.score)

    def start_game(self):
        print("当前玩家%s，开始游戏了" % self.name)
        Game.score += 1

Game.show_help()

g1 = Game("李四")
g1.start_game()

Game.show_top_score()
