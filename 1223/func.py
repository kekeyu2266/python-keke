def printinfo(arg1, *args):
    print(arg1)
    print(args)


printinfo(1, 2, 3)

# 计算累计和


def sumsum(num):
    sum = 0
    if num > 0:
        for n in range(0, num + 1):
            sum = sum + n
        return sum
    elif num < 0:
        for n in range(num, 1):
            sum = sum + n
        return sum
    else:
        return 0


while True:
    num = int(input("请输入一个数字："))
    print(sumsum(num))
