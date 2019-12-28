import random
print("下面生成一个0-1随机数：")

a = random.random()
print(a)

print("下面生成一个100以内的随机数：")
a = random.randint(0, 100)
print(a)


print("下面生成一个1000以内的随机数，必须是13的倍数：")
a = random.randrange(0, 1000, 13)
print(a)
