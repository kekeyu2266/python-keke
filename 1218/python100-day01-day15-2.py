# 练习1：华氏温度转换为摄氏温度
# 提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$

import math as m
f = input("请输入华氏温度数字（仅可输入数字）： ")
f = float(f)


def f2c(f):
    c = (f - 32) / 1.8
    print("华氏温度 %.1f 度 转为摄氏度为 %.1f 度\n" % (f, c))
    return c


f2c(f)

# 练习2：输入圆的半径计算计算周长和面积

r = input("请输入圆的半径： ")
r = float(r)


def yuan(r):
    girth = m.pi * r * 2
    area = m.pi * r ** 2
    print("圆的周长为 %.2f ，圆面积为 %.2f \n" % (girth, area))


yuan(r)

# 练习3：输入年份判断是不是闰年

while True:
    year = input("请输入年份(四位数字，仅可判断1900年至2999年)： ")
    year = int(year)
    if year < 1900 or year > 2999:
        print("\n输入错误，请重新输入\n")
    else:
        break


def yy(year):
    if year % 4 == 0:
        print("%d 年是闰年" % year)
    else:
        print("%d 年不是闰年" % year)


yy(year)
