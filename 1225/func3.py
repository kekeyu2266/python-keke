# 局部变量和全局变量
def test():
    a = 100
    print("test.a=%d" % a)


g_a = 120


def test2():
    g_a = 300
    # a = 100
    # print("test2.a=%d" % a)
    print("test2.g_a=%d" % g_a)


def test3():
    global g_a  # 申明全局变量
    g_a = 333300
    print("test3.g_a=%d" % g_a)


test()
test2()
# print(a)  # a是函数内的局部标亮，全局未定义
print("g_a=%d" % g_a)
test3()
test2()
print("g_a=%d" % g_a)
