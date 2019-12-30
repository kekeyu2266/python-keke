# 整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积，0的阶乘为1。即：n != 1×2×3×...×n。
def jc(n):
    if n > 1:
        sum = n*jc(n-1)
    else:
        sum = 1
    # print(sum)
    return sum


tt = int(input("请输入一个整数吗求阶乘："))
print(jc(tt))
