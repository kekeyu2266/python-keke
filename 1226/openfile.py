from pathlib import Path
import os
print(os.getcwd())
filepath = Path(os.getcwd()) / "11.txt"
print(filepath)
f = open(filepath, "r", encoding="utf-8")
print(f.read())
print(f.tell())
f.close()

f = open(filepath, "r", encoding="utf-8")
print("读取一行".center(50, "-"))
print(f.readline())
print(f.tell())
print("按列表读取所有内容".center(50, "-"))
print(f.readlines())
print(f.tell())
f.close()

print("迭代的方式读取每一行".center(50, "-"))
f = open(filepath, "r", encoding="utf-8")
for i in f:
    print(i)

print(f.tell())
f.close()


with open(filepath, "r", encoding="utf-8") as f:
    print("使用with方式打开并读取文件".center(50, "-"))
    print(f.read())

print(os.listdir())
print(os.getcwdb())
