# U01. 字串分割與匹配的陷阱（2.1–2.11）
#
# 這個檔案示範三個常見的字串處理陷阱：
# 1. 使用 re.split() 時，若分隔符寫成捕獲分組，分隔符會被保留下來。
# 2. startswith() / endswith() 這類方法要接收 tuple，而不是 list。
# 3. strip() 只會移除字串頭尾的空白，不會處理中間的多餘空白。

import re

# ── 捕獲分組保留分隔符（2.1）─────────────────────────
# re.split() 預設會依照規則切割字串；如果分隔規則使用「捕獲分組」
# （也就是括號 (...)），那麼被匹配到的分隔符本身也會出現在結果清單中。
# 這個技巧常用在「切開字串，但仍要保留逗號、分號、空白等分隔符」的情境。
line = "asdf fjdk; afed, fjek,asdf, foo"
# 把空白、分號、逗號當成切割依據；括號表示要把分隔符一併保留下來。
fields = re.split(r"(;|,|\s)\s*", line)
# 切割後的結果會交錯排列：
# 偶數索引是實際文字，奇數索引是分隔符。
values = fields[::2]  # 偶數索引 = 實際值
# 取出每個分隔符，最後再補一個空字串，讓 zip() 可以完整配對最後一段文字。
delimiters = fields[1::2] + [""]
# 依照原順序把文字與分隔符重新接回去。
rebuilt = "".join(v + d for v, d in zip(values, delimiters))
print(rebuilt)  # 'asdf fjdk;afed,fjek,asdf,foo'

# ── startswith 必須傳 tuple（2.2）────────────────────
# startswith() 可以檢查字串是否以某些前綴開頭，但參數必須是「字串」或
# 「tuple of strings」。如果直接傳 list，Python 會丟出 TypeError。
# 這是很多人第一次使用時容易踩到的型別限制。
url = "http://www.python.org"
choices = ["http:", "ftp:"]
try:
    # 這裡刻意示範錯誤用法：list 不能直接拿來給 startswith()。
    url.startswith(choices)  # type: ignore[arg-type]
except TypeError as e:
    # 例外訊息可幫助我們確認問題是參數型別不正確。
    print(f"TypeError: {e}")  # 不能傳 list！
# 正確做法是先把 list 轉成 tuple，讓 startswith() 可以接受。
print(url.startswith(tuple(choices)))  # True（轉成 tuple 才行）

# ── strip 只處理頭尾，不處理中間（2.11）──────────────
# strip() 只會去除字串最左側與最右側的空白字元，
# 不會自動把中間連續的空白壓縮成單一空白。
s = "  hello     world  "
# 只移除頭尾空白；單字之間的多個空白仍會保留。
print(repr(s.strip()))  # 'hello     world'（中間多餘空白還在）
# 如果直接 replace(" ", "")，會把所有空白都刪掉，連單字之間的空白也不見，
# 這通常不是我們想要的結果。
print(repr(s.replace(" ", "")))  # 'helloworld'（過頭，連詞間空白也消）
# 正確作法是先 strip() 去掉頭尾空白，再用正則把中間連續空白壓成一個空白。
print(repr(re.sub(r"\s+", " ", s.strip())))  # 'hello world'（正確）

# 生成器逐行清理（高效，不預載入記憶體）
# 下面這段示範用生成器表達式逐行 strip()：
# - 不需要先把所有資料一次放進記憶體
# - 很適合處理檔案、串流或大量資料
# - 每次迴圈只處理一行，簡潔且省記憶體
lines = ["  apple  \n", "  banana  \n"]
for line in (l.strip() for l in lines):
    # 每次迴圈取得一行已清理過的文字。
    print(line)
