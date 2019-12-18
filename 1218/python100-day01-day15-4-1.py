"""输出乘法口诀表(九九表)

Version: 0.1
Author: 骆昊
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        # 默认print会输入一个\n,需要改写为\t 或者" "
        print("%d*%d=%d " % (i, j, i * j), end="\t")
    print()  # 不写内容，默认输出一个\n
