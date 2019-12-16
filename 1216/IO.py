# 笨办法学python
txt = open(".\\1216\\tt.txt", mode="r", encoding="utf-8")
print(txt.read())
txt.close()
print("-------------")
txt = open(".\\1216\\tt.txt", mode="a", encoding="utf-8")
txt.write("\n4.写点东西")
txt.close()
