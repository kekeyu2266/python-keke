import sys
import func4

print("命令行参数为".center(30, "-"))
for i in sys.argv:
    print(i)

print("python路径为".center(30, "-"))
print(sys.path)

print("导入模块后运行".center(30, "-"))
print(func4.test100(100))
print(func4.test200(15))

print("查看".center(30, "-"))
if __name__ == "__main__":
    print('程序自身在运行')
else:
    print("我来自另一模块")
