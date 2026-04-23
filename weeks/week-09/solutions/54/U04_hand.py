import io
from pathlib import Path

buf = io.StringIO()
print("第一行", file=buf)
print("第二行", file=buf)
print("第三行", file=buf)

text = buf.getvalue()
print("---StringIO 內容---")
print(text)

buf.seek(0)
for i, line in enumerate(buf, 1):
    print(i, line.rstrip())

import csv
mem = io.StringIO()
writer = csv.writer(mem)
writer.writerow(["name", "score"])
writer.writerow(["alice", 90])
print("---CSV in memory---")
print(mem.getvalue())

src = Path("poem.txt")
src.write_text("床前明月光\n\n疑是地上霜\n\n舉頭望明月\n低頭思故鄉\n", encoding="utf-8")

dst = Path("poem_numbered.txt")
with open(src, "rt", encoding="utf-8") as fin, \
     open(dst, "wt", encoding="utf-8") as fout:
    n = 0
    for line in fin:
        line = line.rstrip()
        if not line:
            continue
        n += 1
        print(f"{n:02d}. {line}", file=fout)

print("---加行號後---")
print(dst.read_text(encoding="utf-8"))