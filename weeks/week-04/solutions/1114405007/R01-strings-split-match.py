# R01. 字串分割與匹配（2.1–2.3）
# 這份範例示範三件很常用的事：
# 1. 把一行資料用多種分隔符拆開
# 2. 檢查字串是不是以某個開頭或結尾出現
# 3. 使用類似檔名萬用字元的方式做字串比對
#
# 這些技巧在整理文字資料、讀檔名、過濾路徑或做簡單規則判斷時很常見。

import re
from fnmatch import fnmatch, fnmatchcase

# ── 2.1 多界定符分割 ──────────────────────────────────
# 原始字串中同時混用了空白、分號、逗號。
# 如果只用 split(',') 之類的方法，通常只能處理一種分隔符，
# 但真實資料常常是混在一起，所以這裡使用 re.split()。
line = "asdf fjdk; afed, fjek,asdf, foo"

# [;,\s] 表示「分號、逗號、任一空白字元」三者之一。
# 後面的 \s* 表示分隔符後面若有 0 個到多個空白，也一起吃掉。
# 這樣切完後結果會比較乾淨，不會留下多餘空白。
print(re.split(r"[;,\s]\s*", line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 這裡改用另一種寫法：(?:...) 是「非捕獲分組」。
# 它的作用是把多個選項包成一組，但不把內容另外保留下來。
# 對這個例子來說，效果和上面類似，只是正則表達式的寫法不同。
# 當規則比較複雜時，這種寫法通常更容易讀。
print(re.split(r"(?:,|;|\s)\s*", line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# ── 2.2 開頭/結尾匹配 ────────────────────────────────
# endswith() 與 startswith() 是最直接的前後綴判斷方法。
# 如果只是判斷固定開頭或結尾，通常比正則表達式更清楚。
filename = "spam.txt"
print(filename.endswith(".txt"))  # True
print(filename.startswith("file:"))  # False

# endswith() 可以一次檢查多個可能的副檔名。
# 注意這裡要傳 tuple，不是 list。
# 這在篩選程式碼檔、圖片檔、文字檔時非常常用。
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]
print([name for name in filenames if name.endswith((".c", ".h"))])
# ['foo.c', 'spam.c', 'spam.h']

# ── 2.3 Shell 通配符匹配 ─────────────────────────────
# fnmatch() 提供像作業系統檔名比對那樣的萬用字元規則。
# *.txt 表示「任意字串 + .txt 結尾」。
print(fnmatch("foo.txt", "*.txt"))  # True

# Dat[0-9]* 表示：
# 1. 先以 Dat 開頭
# 2. 接著一個數字字元
# 3. 後面再接任意長度的任意字元
print(fnmatch("Dat45.csv", "Dat[0-9]*"))  # True

# fnmatch() 在某些系統上可能會受平台大小寫規則影響。
# 如果你想明確要求「大小寫要完全一致」，就用 fnmatchcase()。
print(fnmatchcase("foo.txt", "*.TXT"))  # False

# 這裡過濾所有以 ST 結尾的地址。
# * ST 的意思是：前面可以有任意內容，但最後必須是空白加 ST。
addresses = ["5412 N CLARK ST", "1060 W ADDISON ST", "1039 W GRANVILLE AVE"]
print([a for a in addresses if fnmatchcase(a, "* ST")])
# ['5412 N CLARK ST', '1060 W ADDISON ST']
