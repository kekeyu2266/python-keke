import os
from sys import path, argv
from test_module2 import haha2
import test_module
from pathlib import Path  # 解决Mac与Windows系统文件路径分隔符不一致的问题

# 复习文件打开
print(os.getcwd())  # 当前目录是文件所在的上一级目录？
folder = Path(os.getcwd()) / "tt.txt"  # 解决Mac与Windows系统文件路径分隔符不一致的问题
print(folder)
tt = open(folder, mode="r", encoding="utf-8")
print(tt.read())
tt.close()


# a模式打开文件，指针在文件结尾，无法使用read（）读取
tt = open(folder, "a", encoding="utf-8")
tt.write("\n5.你这个垃圾!\n------")
tt.close()

tt = open(folder, mode="r", encoding="utf-8")
print(tt.read())
tt.close()

# 模块导入
test_module.haha()  # func_name使用import导入函数，必须要加模块名称
haha2()  # 使用from module_name import func_name,可以直接使用

print(path, "\n------")

print(argv, "\n-----")
