# R01 字串分割與樣式比對
# 主題：re.split()、startswith()、endswith()、fnmatch()

import re
from fnmatch import fnmatch, fnmatchcase

# 範例字串：同時包含分號、逗號與空白，常見於「混合分隔符」資料清理情境。
line = "asdf fjdk; afed, fjek,asdf, foo"

# 1) 使用字元集合 [;,\s] 表示「分號、逗號或空白」任一分隔符。
#    後面的 \s* 代表分隔符後方若有多餘空白，也一併吃掉。
print(re.split(r"[;,\s]\s*", line))

# 2) 功能等價的寫法：(?:,|;|\s) 是「非捕獲群組」的 OR 寫法。
#    與上方差異只在正規表達式風格，結果相同。
print(re.split(r"(?:,|;|\s)\s*", line))

# 3) 使用 startswith/endswith 判斷字串前綴與副檔名。
filename = "spam.txt"
print(filename.endswith(".txt"))
print(filename.startswith("file:"))

# 4) endswith 可接受 tuple，一次比對多種副檔名。
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]
print([name for name in filenames if name.endswith((".c", ".h"))])

# 5) fnmatch 使用 Shell 風格萬用字元（*、?、[0-9]）。
print(fnmatch("foo.txt", "*.txt"))
print(fnmatch("Dat45.csv", "Dat[0-9]*"))

# 6) fnmatchcase 會嚴格區分大小寫。
print(fnmatchcase("foo.txt", "*.TXT"))

addresses = ["5412 N CLARK ST", "1060 W ADDISON ST", "1039 W GRANVILLE AVE"]
# 只留下地址尾碼為 ST 的項目。
print([a for a in addresses if fnmatchcase(a, "* ST")])
