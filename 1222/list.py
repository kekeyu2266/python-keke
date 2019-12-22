A = ['xiaoWang', 'xiaoZhang', 'xiaoHua']

print("-"*30)
name = input("请输入姓名：")
A.append(name)
print(A)
print("-" * 30)

name = input("请输入要修改的第一个姓名：")
A[0] = name  # 直接修改列表第一个元素的值
print(A)
print("-" * 30)

name = input("请输入要查询的姓名：")
if name in A:
    print("Yes")
else:
    print("没有找到")
print("-" * 30)

name = input("要删除的值：")
if name in A:
    A.remove(name)
    print(A)
else:
    print("No")
print("-" * 30)

i = 0
for name in A:
    print("%d %s" % (i, name))
    i = i + 1

index = input("\n请输入要删除的姓名序号:")
index = int(index)
# del A[index]
A.pop(index)
print(A)
