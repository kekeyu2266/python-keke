# 交换变量
a = input("请输入a：")
b = input("请输入b：")
c = a
a = b
b = c
print("交换后，a为%s，b为%s" % (a, b))

# 不借助临时变量进行交换
a = input("请输入a：")
b = input("请输入b：")
c = a
a, b = b, a
print("交换后，a为%s，b为%s" % (a, b))
