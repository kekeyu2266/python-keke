# 名片管理器
import time
names = ["haha", "hehe", "hzhz", "lala"]
print("\n------欢迎进入名片管理系统------")
while True:
    n = input(
        "请输入数字选择要进行的操作，按回车确认：\n\n1 显示名片清单\n2 新增人员\n3 删除人员\n4 修改人员\n5 查找人员\n按其他任意键退出\n")
    if n not in ["1", "2", "3", "4", "5"]:
        print("程序退出，再见")
        break
    n = int(n)
    if n == 1:
        print("\n------查询中------\n")
        time.sleep(1)
        print("\n人员名单如下：")
        for i in names:
            print(i)
        print("\n------查询完毕------\n")
    elif n == 2:
        new = input("请输入要增加的人员姓名：")
        names.append(new)
        print("\n------添加中------\n")
        time.sleep(1)
        print("\n------添加成功------")
        print("新的人员名单如下：")
        for i in names:
            print(i)
        print("\n------添加完毕------")
    elif n == 3:
        time.sleep(1)
        j = 0
        for i in names:
            print("%d--%s" % (j, i))
            j += 1
        dd = input("\n请输入要删除的人员序号：")
        dd = int(dd)
        del names[dd]
        print("\n------删除中------\n")
        time.sleep(1)
        print("删除成功，最新人员名单如下：")
        for i in names:
            print(i)
        print("\n------删除完毕------")
    elif n == 4:
        j = 0
        print("\n------查询中------\n")
        time.sleep(1)
        for i in names:
            print("%d--%s" % (j, i))
            j += 1
        xx = int(input("请输入要修改的人员序号："))
        yy = input("请输入新的姓名：")
        print("\n------更新中------\n")
        time.sleep(1)
        names[xx] = yy
        print("\n更新成功，新的人员名单如下：\n")
        for i in names:
            print(i)
        print("\n------更新完毕------")
    elif n == 5:
        nn = input("请输入要查询的姓名：")
        print("\n------查询中------\n")
        time.sleep(1)
        if nn in names:
            print("yes,该姓名序号为%d" % (names.index(nn) + 1))
        else:
            print("查无此人\n")
