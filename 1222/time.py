import time
import calendar
import random as rr
tt = time.time()
print(tt)
tt = time.localtime(tt)
print(tt)
print(type(tt))
tt = time.asctime(tt)
print(tt, "类型：", type(tt))

r = rr.randint(0, 12)
print(r)
u = rr.uniform(1, 5)
print(u)

r = rr.randrange(0, 51, 2)
print(r)
