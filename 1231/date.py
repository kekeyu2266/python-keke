# 时间模块
import datetime
dd = datetime.datetime.now()
print(type(dd))
print("这里是分割线".center(30, "*"))
print(dir(datetime))
print("这里是分割线".center(30, "*"))
print(dir(datetime.datetime))
print(dd)
print("这里是分割线".center(30, "*"))
print(dd.year)
print(dd.month)
print(dd.day)
print("这里是分割线".center(30, "*"))
print(dd.strftime("%A"))  # %A	Weekday，完整版本

# 创建一个日期时间实例
tt = datetime.datetime(2009, 10, 26)  # 纯数字
print(tt)
print(tt.strftime("%W"))
