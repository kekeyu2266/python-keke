# 文件的读取
import os
from pathlib import Path
filepath1 = Path(os.getcwd()) / "22.txt"
with open(filepath1, "r", encoding="utf-8") as ff:
    # print(ff.readlines())
    ll = ff.readlines()
    for n in ll:
        print(n)

print("这个是分割线".center(30, "*"))
with open(filepath1, "r") as ff:
    cc = ff.readline()
    while len(cc) > 0:
        cc = ff.readline()
        print(cc)

with open(filepath1, "r") as ff:
    print("文件一共%d行" % len(ff.readlines()))
