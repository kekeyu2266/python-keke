# 求圆的面积
import math
math.pi
while True:
    try:
        r = float(input("请输入圆的半径："))
        s = math.pi*r**2
        break
    except ValueError:
        print("输入错误")
print("圆的半径为%f，面积为%f" % (r, s))
