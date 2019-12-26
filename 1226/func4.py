# 函数的递归
def a():
    print("-" * 20)


def b():
    print("-" * 10)
    b()


def test1(num):
    i = 1
    sum = 0
    while i <= num:
        sum = sum + i
        i += 1
    return sum


def test2(num):
    i = 1
    sum = 1
    while i <= num:
        sum = sum * i
        i += 1
    return sum


def test100(num):
    if num >= 1:
        sum = num + test100(num - 1)
    else:
        sum = 0
    return sum


def test200(num):
    if num > 1:
        sum = num * test200(num - 1)
    else:
        sum = 1
    return sum


print(test1(100))
print(test100(100))
print(test2(13))
print(test200(13))

print("查看".center(30, "-"))
if __name__ == "__main__":
    print('程序自身在运行')
else:
    print("我来自另一模块")
