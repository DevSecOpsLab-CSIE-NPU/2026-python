# U01. 字串分割與匹配的陷阱（2.1–2.11）
# 這份範例主要示範三個容易踩雷的地方：
# 1. 使用 re.split() 時，如果正則包含捕獲群組，分隔符也會留在結果裡。
# 2. startswith() / endswith() 想一次比對多個前綴時，參數必須用 tuple。
# 3. strip() 只會清理字串頭尾，不會自動處理中間的空白。

import re

# ── 捕獲分組保留分隔符（2.1）─────────────────────────
# re.split() 的規則是：只要正則裡有捕獲群組，群組匹配到的內容也會被放回清單。
# 這代表回傳值不只是切好的欄位，還會混入分隔符，所以後續通常要再拆分一次。
line = "asdf fjdk; afed, fjek,asdf, foo"
fields = re.split(r"(;|,)\s*", line)

# fields 的結構會像：[值, 分隔符, 值, 分隔符, ...]。
# 因此可以用切片把資料欄位與分隔符分開處理。
values = fields[::2]  # 偶數索引是實際文字內容
delimiters = fields[1::2] + [""]  # 補一個空字串，避免最後一段沒有對應分隔符

# 把值和分隔符重新配對後再串回去，就能保留原本的分隔邏輯。
rebuilt = "".join(v + d for v, d in zip(values, delimiters))
print(rebuilt)  # 'asdf fjdk;afed,fjek,asdf,foo'

# ── startswith 必須傳 tuple（2.2）────────────────────
# startswith() 可以一次檢查多個候選前綴，但它要求傳入 tuple，不能直接給 list。
# 這是因為 API 的設計是接受「不可變」的選項集合，而不是可變容器。
url = "http://www.python.org"
choices = ["http:", "ftp:"]

try:
    # 這裡刻意示範錯誤用法：直接把 list 傳進去會觸發 TypeError。
    url.startswith(choices)  # type: ignore[arg-type]
except TypeError as e:
    print(f"TypeError: {e}")  # 不能直接傳 list

# 改成 tuple 之後就能正常使用，startswith() 會依序比對每個候選前綴。
print(url.startswith(tuple(choices)))  # True

# ── strip 只處理頭尾，不處理中間（2.11）──────────────
# strip() 只會移除字串左右兩端的指定字元，預設是空白字元。
# 它不會修改字串中間的空白，所以不能拿來當成「壓縮所有空白」的工具。
s = "  hello     world  "

# strip() 只去掉頭尾的空白，中間多個空白仍然保留。
print(repr(s.strip()))

# replace(" ", "") 會把所有空白都刪掉，連單字之間本來該保留的分隔也一起消失。
print(repr(s.replace(" ", "")))

# 先 strip() 去頭尾，再用正則把中間連續空白壓成單一空白，才是常見的正確做法。
print(repr(re.sub(r"\s+", " ", s.strip())))

# ── 生成器逐行清理（高效，不預載入記憶體）──────────────
# 如果資料很多，最好用生成器逐行處理，避免一次把全部內容塞進記憶體。
# 下面的寫法會在迭代時才對每一列執行 strip()，屬於延遲求值。
lines = ["  apple  \n", "  banana  \n"]
for line in (l.strip() for l in lines):
    print(line)
