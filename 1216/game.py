# coding=utf-8
# 石头剪刀布游戏

import random
upc = random.randint(0, 2)
player = input("请输入 剪刀(0)  石头(1) 布(2)")
player = int(player)
if (player == 0 and upc == 2) or (player == 1 and upc == 0) or(player == 2 and upc == 1):
    print("upc = %d,你赢了" % upc)
elif player == upc:
    print("upc = %d,平局" % upc)
else:
    print("upc = %d,你输了" % upc)
