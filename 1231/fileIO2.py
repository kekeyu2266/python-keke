import os
from pathlib import Path
filepath1 = Path(os.getcwd()) / "22.txt"
print(filepath1)

with open(filepath1, "r", encoding="utf-8") as f:
    print(f.read(6))
    print("这个是分割线".center(30, "*"))
    print(f.read(6))
