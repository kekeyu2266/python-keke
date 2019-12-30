# 质数判断
# 一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等）
while True:
    try:
        n = int(input("请输入一个整数:"))
        break

    except ValueError:
        print("输入错误：")


def vs(n):
    for i in range(2, n):
        if n % i == 0:
            print("不是质数")
            return False
            break
        else:
            continue
    print("质数")
    return True


vs(n)
