inn = {"aa": 11, "bb": 22}
print("显示字典内容".center(30, "-"),)
print(inn.keys())
print(inn.values())
print("迭代字典".center(30, "-"),)
for n in inn:  # 使用for循环字典，默认迭代字典的key值
    print(n)
print("迭代字典的key值".center(30, "-"))
for kk in inn.keys():
    print(kk)
print("-"*10)
for vv in inn.values():
    print(vv)
print("-"*10)
for it in inn.items():
    print(it)
print("-"*10)
for kk, vv in inn.items():
    print("%s = %d" % (kk, vv))

print("-" * 10)

confusion = {}
confusion[1] = 1
confusion['1'] = 2
confusion[1] += 1

print(confusion)
print("*" * 10)
sum = 0
for k in confusion:
    print(k)
    sum += confusion[k]

print(sum)
