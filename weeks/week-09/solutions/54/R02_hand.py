import os
from pathlib import Path

base = Path("weeks") / "week-09"
print(base)
print(base.name)
print(base.parent)
print(base.suffix)

f = Path("hello.txt")
print(f.stem, f.suffix)

print(os.path.join("weeks", "week-09", "README.md"))

p = Path("hello.txt")
print(p.exists())
print(p.is_file())
print(p.is_dir())

missing = Path("no_such_file.txt")
if not missing.exists():
    print(f"{missing} 不存在，略過讀取")

here = Path(".")

for name in os.listdir(here):
    print("listdir:", name)

for p in here.glob("*.py"):
    print("glob:", p)

for p in Path("..").rglob("*.py"):
    print("rglob:", p)
    break