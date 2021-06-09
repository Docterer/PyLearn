str_header = "*" * 50
str_title = "\t欢迎使用飞机程序\t"
str_tail = "*" * 50

card_list = []


def show_menu():
    print(str_header)
    print(str_tail)


def add_card(name, age):
    card = {}
    card.setdefault("name", name)
    card.setdefault("age", age)
    card_list.append(card)


def show_list():
    print(card_list)


def test():
    for a in [1, 2, 3, 4, 5]:
        if a == 3:
            return
        print(a)


while True:
    show_menu()
    name = input("请输入添加的用户名:")
    age = int(input("请输入年龄："))
    add_card(name=name, age=age)
    show_list()
    test()
