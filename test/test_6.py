# Python 判断字符串是否为数字
try:
    n = float(input("请输入 ："))

    print("是数字")


except ValueError:
    print("不是数字")
