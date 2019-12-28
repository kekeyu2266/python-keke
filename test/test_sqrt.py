# 求平方根
import math
while True:
    try:
        n = input("请输入一个需要开平方的整数：")
        n = int(n)
        break
    except ValueError:
        print("输入错误")
re = math.sqrt(n)
print(re)
