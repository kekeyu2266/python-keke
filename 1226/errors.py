while True:
    try:
        x = int(input("请输入一个数字："))
        break
    except (ValueError, KeyboardInterrupt):
        print("不是数字，请重新输入~！")
