import random
import math
import sys
print(sys.argv)

aa = random.choice(["34", "gdd", "adf"])  # 随机多选一
print(aa)
bb = random.randrange(0, 100, 20)  # 随机数字，指定递增步长
print(bb)
cc = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                    12, 13, 14, 15, 16, 17, 18, 19, 20], 4)  # 随机多选多，指定选择数量
print(cc)
