from urllib.request import urlopen
i = 0

for line in urlopen("https://kekeyu.gitee.io/"):
    line = line.decode("utf-8")
    i = i + 1
    if i > 30:
        break
    print(line)
