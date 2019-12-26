import shutil
import os


p = os.getcwd()
print(p)
os.chdir("c:\\")  # 改变当前运行目录
p = os.getcwd()
print(p)
os.mkdir("123\\")
# os.chdir("123\\")
pp = os.getcwd()
print(pp)
p2 = dir(os)
print(p2)
print("-"*30)
p3 = os.listdir(os.getcwd())
print(p3)


shutil.move("\\123", "\\1234")
