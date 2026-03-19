# R01. 字串分割與匹配（範例 2.1–2.3）
import re
from fnmatch import fnmatch, fnmatchcase

# ── 2.1 使用正則表達式進行多界定符分割 ──
line = "asdf fjdk; afed, fjek,asdf, foo"
# 使用 re.split 可以一次指定多個分隔符（分號、逗號、空格）
# [;,\s]\s* 代表匹配分號、逗號或空白，後面跟著任意數量的空白
print(re.split(r"[;,\s]\s*", line))

# 技巧：非捕獲分組 (?:...)
# 如果正則使用了括號 ( )，分隔符會被保留在結果中；使用 (?:...) 則不會保留分隔符
print(re.split(r"(?:,|;|\s)\s*", line))

# ── 2.2 檢查字串開頭或結尾 ──
filename = "spam.txt"
print(filename.endswith(".txt"))  # True
print(filename.startswith("file:"))  # False

# 同時檢查多種可能性：必須傳入 tuple（元組），不能用 list
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]
print([name for name in filenames if name.endswith((".c", ".h"))])
# 輸出：['foo.c', 'spam.c', 'spam.h']

# ── 2.3 使用 Shell 通配符匹配字串 ──
# 這在過濾檔名時非常方便，不需要寫複雜的正則
print(fnmatch("foo.txt", "*.txt"))  # True (忽略或遵守系統大小寫規定)
print(fnmatchcase("foo.txt", "*.TXT"))  # False (強制區分大小寫)