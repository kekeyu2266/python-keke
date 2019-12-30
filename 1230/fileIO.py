# 打开文件
from pathlib import Path
import os
filepath1 = Path(os.getcwd()) / "11.txt"
filepath2 = Path(os.getcwd()) / "123.png"
print(filepath1)
print(filepath2)
with open(filepath1, "r", encoding="utf-8") as ff:
    print(ff.read())
print("这个是分割线".center(30, "-"))
with open(filepath1, "a", encoding="utf-8") as ff:
    ff.write("\nhahaha")
with open(filepath1, "r", encoding="utf-8") as ff:
    print(ff.read())
