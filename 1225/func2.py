# 函数的嵌套调用
def print1(num, str1):
    print(str1 * num)


def print2(num, str1, line):
    while line > 0:
        print1(num, str1)
        line -= 1


print2(22, "*", 5)


def sum3(*arvg):
    sum = 0
    for n in arvg:
        sum = sum + n
    print(sum)
    return sum


def av3(*arvg):
    n = len(arvg)
    av = sum3(*arvg) / n
    print(av)
    return av


av3(1, 2, 3, 4, 5, 6)
