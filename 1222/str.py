names = ["3254q5234561", "asdgafdsgh agasd2", "3wetadsgadf3", "ewtgarsdhadt4"]
i = 0
for n in names:
    print(n)
    i = i+1

print("------")

i = 0
while i < len(names):
    # print(names[i])
    print("names[%d]=%s" % (i, names[i]))
    i += 1

ss = "qwerty"
for i in ss:  # 正序
    print(i)
print("-" * 10)

i = len(ss)-1  # 倒序
while i >= 0:
    print(ss[i])
    i -= 1
