# 求中位数
import numpy


def vs(*arvg):
    l1 = list(arvg)
    n = len(l1)
    l1.sort()
    m = n//2
    if n % 2 == 0:
        return (l1[m-1]+l1[m])/2
    else:
        return l1[m]


l1 = [1, 2, 888, 3, 4, 5, 6]
l2 = [1, 2, 3, 888, 4, 5]

print(vs(1, 2, 888, 3, 4, 5, 6))
print(vs(1, 2, 3, 888, 4, 5))
print(numpy.median(l1))  # 调用numpy中的中位数函数来计算验证结果
print(numpy.median(l2))
