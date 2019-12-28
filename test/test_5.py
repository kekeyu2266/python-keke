# 以下实例通过使用 if...elif...else 语句判断数字是正数、负数或零：
while True:
    try:
        n = float(input("请输入一个整数："))
        break
    except ValueError:
        print("输入错误")
if n > 0:
    print("正数")

elif n < 0:
    print("负数")
else:
    print("零")
