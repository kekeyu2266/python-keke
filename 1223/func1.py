# coding=utf-8
#!/usr/local/bin/python3


def test():
    print("\n", "*"*10, "这里是分割线", "*"*10, "\n")


test()


def aa(num1, *argv):  # 可变参数，可变参数是0个或者多个，传入的是一个tuple
    for n in argv:
        print(n)
        print(num1)


aa("-----", 2, 5, 7, 3, 5,)
test()


def test2(name, age=19):  # 默认参数
    print(name, age)


test2("keke", 19)
test2("haha")  # 可以不传入默认参数
test2("didi", 20)  # 可以传入默认参数，以传入值为准
test2(age=22, name="lala")  # 可以指定参数名称，顺序就可以乱了
