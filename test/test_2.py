# 一元二次方程求解
import math
while True:
    try:
        a = input("请输入a的值：")
        if float(a) == 0:
            print("a不可为0")
            continue
        b = input("请输入b的值：")
        c = input("请输入c的值：")
        a = float(a)
        b = float(b)
        c = float(c)
        n = math.sqrt(b * b - 4 * a * c)
        break
    except ValueError:
        print("错误的输入值")
n = math.sqrt(b * b - 4 * a * c)

x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
print(x1, x2)
