from pathlib import Path
import os

while True:
    try:
        filename = input("\n请输入需要复制的文件名：\n")
        filename_plus = filename.split(".")
        filepath = Path(os.getcwd()) / filename
        # print(filepath)
        with open(filepath, "r", encoding="utf-8") as ff:
            hh = ff.readline()
            with open(filename_plus[0] + "复制"+str(i)+"."+filename_plus[1], "w", encoding="utf-8") as dd:
                while len(hh) > 0:
                    dd.write(hh)
                    hh = ff.readline()
        break
    except FileNotFoundError or PermissionError:
        print("该文件不存在，请重新输入".center(50, "*"))
