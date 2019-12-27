# 数字求和
while True:
    try:
        nums = input("请输入需要求和的数字，用逗号隔开，回车结束：")
        nums = nums.split(",")
        nums2 = []
        for n in nums:
            nums2.append(float(n))
        print(nums2)
        break
    except ValueError:
        print("输入错误,请确保输入的是数字")


def sums(arvg):
    sums = 0
    for i in arvg:
        sums += i
    return sums


print("求和结果为：%f" % sums(nums2))
