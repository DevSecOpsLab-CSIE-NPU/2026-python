from pathlib import Path

path = Path("hello.txt")
with open(path, "wt", encoding="utf-8") as f:
    f.write("你好，Python\n")
    f.write("第二行\n")

with open(path, "rt", encoding="utf-8") as f:
    print(f.read())

with open(path, "rt", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip())

with open("log.txt", "wt", encoding="utf-8") as f:
    print("登入成功", file=f)
    print("使用者:", "alice", file=f)

fruits = ["apple", "banana", "cherry"]
with open("fruits.csv", "wt", encoding="utf-8") as f:
    print(*fruits, sep=",", end="\n", file=f)

with open("fruits.csv", "at", encoding="utf-8") as f:
    print("date", end=",", file=f)
    print("2026-04-23", file=f)

print(Path("fruits.csv").read_text(encoding="utf-8"))

try:
    with open("bad.txt", "wt", encoding="utf-8") as f:
        f.write(b"bytes in text mode")
except TypeError as e:
    print("錯誤示範:", e)