# 求最大数和最小数
while True:
    try:
        arvg = input("请输入几个数字，用逗号分隔：")
        arvg = arvg.split(",")
        list1 = []
        for n in arvg:
            n = float(n)
            list1.append(n)
        break
    except ValueError:
        print("输入值错误")


def max(arvg):
    max = arvg[0]
    for n in arvg:
        if max < n:
            max = n
    print("最大值：%f" % max)
    return max


def min(arvg):
    min = arvg[0]
    for n in arvg:
        if min > n:
            min = n
    print("最小值：%f" % min)
    return min


max(list1)
min(list1)
