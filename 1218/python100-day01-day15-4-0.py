"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
import random as r
answer = r.randint(1, 100)
lala = int(input("我已经有答案了，请输入一个数字来猜(答案是1到100之间的一个整数)： "))
count = 0
while count < 10:
    if lala > answer:
        print("猜大了,再来\n")
        lala = int(input("请再猜： "))
        count += 1
        continue
    elif lala < answer:
        print("猜小了，再来\n")
        lala = int(input("请再猜： "))
        count += 1
        continue
    else:
        if count < 7:
            print("\n恭喜你猜对了，只用了%d次，你真是天才！答案就是:%d \b" % (count, answer))
            break
        else:
            print("\n恭喜你猜对了！答案就是:%d ,用了%d次 ,你还需努力\n" % (answer, count))
            break
if count >= 10:
    print("\n不好意思次数已经用尽了，你太笨了！答案是:%d \n" % answer)
