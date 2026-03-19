"""
R01: 字串切割與比對

示範 re.split、startswith、endswith 與 fnmatch。
"""

import re
from fnmatch import fnmatch, fnmatchcase


# 2.1 用多種分隔符號切字串
line = "asdf fjdk; afed, fjek,asdf, foo"
print(re.split(r"[;,\s]\s*", line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 非捕獲群組也能達到相同效果。
print(re.split(r"(?:,|;|\s)\s*", line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 2.2 檢查開頭與結尾
filename = "spam.txt"
print(filename.endswith(".txt"))      # True
print(filename.startswith("file:"))   # False

# endswith 可以一次接多個副檔名，但型別要是 tuple。
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]
print([name for name in filenames if name.endswith((".c", ".h"))])
# ['foo.c', 'spam.c', 'spam.h']

# 2.3 用 shell 風格做樣式比對
print(fnmatch("foo.txt", "*.txt"))          # True
print(fnmatch("Dat45.csv", "Dat[0-9]*"))    # True

# fnmatchcase 會區分大小寫。
print(fnmatchcase("foo.txt", "*.TXT"))      # False

addresses = ["5412 N CLARK ST", "1060 W ADDISON ST", "1039 W GRANVILLE AVE"]
print([a for a in addresses if fnmatchcase(a, "* ST")])
# ['5412 N CLARK ST', '1060 W ADDISON ST']
