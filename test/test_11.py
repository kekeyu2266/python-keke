# 十进制转二进制、八进制、十六进制
while True:
    try:
        n = int(input("请输入一个整数："))
        break
    except ValueError:
        print("输入错误")

print("十六进制为：", hex(n))
print("八进制为：", oct(n))
print("二进制为：", bin(n))
print("%d 的十六进制为：%x" % (n, n))
print("%d 的八进制为：%o" % (n, n))
# print("%d 的二进制为：%b" % (n, n))
