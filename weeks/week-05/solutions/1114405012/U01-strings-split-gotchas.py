# U01. 字串分割與匹配的陷阱（2.1–2.11）
# 捕獲分組保留分隔符 / startswith 必須傳 tuple / strip 只處理頭尾

import re

# ── 捕獲分組保留分隔符（2.1）─────────────────────────
# re.split() 預設會把分隔符丟掉；如果把分隔符放進括號，
# 就會把分隔符也保留下來，方便我們之後重新組回原本的字串。
# 這種寫法常用在「要拆開分析，但還想保留原本分隔方式」的情境。
line = "asdf fjdk; afed, fjek,asdf, foo"
fields = re.split(r"(;|,|\s)\s*", line)
# fields 會變成「文字、分隔符、文字、分隔符...」交錯排列。
# 偶數索引是實際文字，奇數索引是分隔符號。
values = fields[::2]
delimiters = fields[1::2] + [""]  # 最後補一個空字串，避免 zip 時少接一段
rebuilt = "".join(v + d for v, d in zip(values, delimiters))
print("重建後的字串：", rebuilt)  # asdf fjdk;afed,fjek,asdf,foo

# ── startswith 必須傳 tuple（2.2）────────────────────
# startswith() 可以一次檢查多個開頭，但參數必須是 tuple，
# 不能直接丟 list。這是因為 startswith() 的設計是接受一組不可變的候選值。
# 如果傳 list，Python 會直接丟出 TypeError。
url = "http://www.python.org"
choices = ["http:", "ftp:"]
try:
    url.startswith(choices)  # type: ignore[arg-type]
except TypeError as e:
    print(f"發生錯誤：{e}")  # 這裡故意示範錯誤：list 不能直接用
# 先把 list 轉成 tuple，startswith() 就能正常判斷是否以任一前綴開頭。
print("轉成 tuple 後的結果：", url.startswith(tuple(choices)))  # True

# ── strip 只處理頭尾，不處理中間（2.11）──────────────
# strip() 只會移除字串頭尾的空白，對中間的空白完全不會動作。
# 如果只是呼叫 strip()，像多個單字之間的多餘空白仍然會保留。
# 如果直接 replace(" ", "")，又會把所有空白都刪掉，連單字之間的分隔也消失。
s = "  hello     world  "
print("strip() 之後：", repr(s.strip()))  # 'hello     world'
print("replace(' ', '') 之後：", repr(s.replace(" ", "")))  # 'helloworld'
# 比較合理的做法是先 strip() 去掉頭尾，再用正規表示式把中間的多個空白合併成一個。
print("整理成單一空白後：", repr(re.sub(r"\s+", " ", s.strip())))  # 'hello world'

# 生成器逐行清理（高效，不預載入記憶體）
# 如果資料很多，不建議先一次全部做成乾淨版本，因為會浪費記憶體。
# 這裡用生成器逐行 strip()，邊走邊處理，適合大量文字資料的清理工作。
lines = ["  apple  \n", "  banana  \n"]
for line in (l.strip() for l in lines):
    print("清理後的行：", line)
