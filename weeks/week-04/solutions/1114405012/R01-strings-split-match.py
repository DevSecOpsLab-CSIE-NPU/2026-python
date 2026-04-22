# R01. 字串分割與匹配（2.1–2.3）
# re.split() 多分隔符 / startswith / endswith / fnmatch

import re
from fnmatch import fnmatch, fnmatchcase


def section(title: str) -> None:
    print(f"\n=== {title} ===")

# ── 2.1 多界定符分割 ──────────────────────────────────
line = "asdf fjdk; afed, fjek,asdf, foo"
section("2.1 多界定符分割")

# 字元集合 [;,\s] 表示「分號、逗號或空白」，後面的 \s* 吃掉分隔符後多餘空白。
print("原始字串:", line)
print("re.split 結果:", re.split(r"[;,\s]\s*", line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 非捕獲分組：分組但不保留分隔符
print("非捕獲分組 split:", re.split(r"(?:,|;|\s)\s*", line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# ── 2.2 開頭/結尾匹配 ────────────────────────────────
filename = "spam.txt"
section("2.2 開頭與結尾匹配")
print("檔名:", filename)
print("endswith('.txt'):", filename.endswith(".txt"))  # True
print("startswith('file:'):", filename.startswith("file:"))  # False

# 同時檢查多種後綴 → 傳入 tuple（不能傳 list）
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]
print("符合 .c/.h 的檔案:", [name for name in filenames if name.endswith((".c", ".h"))])
# ['foo.c', 'spam.c', 'spam.h']

# ── 2.3 Shell 通配符匹配 ─────────────────────────────
section("2.3 Shell 通配符匹配")
print("fnmatch('foo.txt', '*.txt'):", fnmatch("foo.txt", "*.txt"))  # True
print("fnmatch('Dat45.csv', 'Dat[0-9]*'):", fnmatch("Dat45.csv", "Dat[0-9]*"))  # True

# fnmatchcase 強制區分大小寫
print("fnmatchcase('foo.txt', '*.TXT'):", fnmatchcase("foo.txt", "*.TXT"))  # False

addresses = ["5412 N CLARK ST", "1060 W ADDISON ST", "1039 W GRANVILLE AVE"]
print("結尾是 ' ST' 的地址:", [a for a in addresses if fnmatchcase(a, "* ST")])
# ['5412 N CLARK ST', '1060 W ADDISON ST']
