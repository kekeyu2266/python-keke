print("这个放在中间".center(20, "-"))

# 数据在计算机中是按补码来运算的，运算结束的结果依然是补码

# 正数的原码反码补码都一致
# 负数的原码转为补码，符号位不变，其他位取反，然后再加一

num = -0b00000010  # 0b开头相当于二进制赋值
print(num)
num1 = num << 3  # 相当于乘2的3次方
print(num1)
num2 = num >> 1  # 相当于除2的1次方
print(num2)

num = 4
num2 = ~num  # 取反位运算
print(num2)

num = -4
num2 = ~num  # 取反位运算
print(num2)
print("这个放在中间".center(20, "-"))
num = oct(1000)
print(num)
num = bin(100)
print(num)
num = hex(100)
print(num)
