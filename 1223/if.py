# Fibonacci series: 斐波纳契数列
a, b = 0, 1
while b < 1000:
    print(b, end=",")
    a, b = b, a + b
print("-"*15)
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print("循环结束")

print("-"*15)
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print("循环结束")


if None:
    print("Hello")
