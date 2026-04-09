# U01. 字串分割與匹配的陷阱（2.1–2.11）
# 捕獲分組保留分隔符 / startswith 必須傳 tuple / strip 只處理頭尾
# 本檔主軸：看似常用的字串 API，在真實資料處理時常有細節陷阱。
# 這份版本把每個步驟拆開說明，方便之後重看時快速回想觀念。

import re

# ── 捕獲分組保留分隔符（2.1）─────────────────────────
# 這行模擬一筆混合「空白、分號、逗號」作為分隔符的資料。
# 真實世界中，像是匯入舊資料或處理半結構化文字時，很常遇到這種情況。
line = "asdf fjdk; afed, fjek,asdf, foo"

# 重點：re.split() 如果 pattern 裡面用了「捕獲群組 ()」，
# 那麼不只會切開字串，連「分隔符本身」也會一起保留下來。
# 這很適合拿來做「切開後仍然想知道原本是用什麼符號隔開」的情境。
fields = re.split(r"(;|,|\s)\s*", line)

# fields 的結果會長得像：
# ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
# 偶數索引位置是實際資料值，奇數索引位置是分隔符。
values = fields[::2]  # 0, 2, 4... 取出真正的內容值

# 分隔符數量通常會比值少 1，所以最後補上一個空字串，
# 這樣等等做 zip() 重組時，長度才能對得起來。
delimiters = fields[1::2] + [""]

# 把資料值與分隔符一一配對後重新組裝。
# 注意：因為 split 的正規表達式同時把分隔符後面的多餘空白吃掉了，
# 所以 rebuilt 會是緊湊版本，不會完全等於原字串的空白樣式。
rebuilt = "".join(v + d for v, d in zip(values, delimiters))
print(rebuilt)  # 'asdf fjdk;afed,fjek,asdf,foo'

# ── startswith 必須傳 tuple（2.2）────────────────────
# 想一次檢查網址是不是多種前綴之一，是常見需求。
url = "http://www.python.org"
choices = ["http:", "ftp:"]
try:
    # 這裡故意示範錯法：startswith 的第二種用法只接受 tuple，
    # 不接受 list、set 等其他可迭代物件。
    url.startswith(choices)  # type: ignore[arg-type]
except TypeError as e:
    print(f"TypeError: {e}")  # 不能直接傳 list

# 正確作法：把 list 轉成 tuple 後再傳入。
# 這樣 startswith 會幫你判斷「只要符合其中任一前綴即可」。
print(url.startswith(tuple(choices)))  # True（轉成 tuple 才行）

# ── strip 只處理頭尾，不處理中間（2.11）──────────────
# 很多人第一次看到 strip 時，會誤以為它能清掉所有空白；其實不是。
s = "  hello     world  "

# strip() 只會處理字串兩端，也就是前導空白與尾端空白。
# 中間那些連續空白完全不會動。
print(repr(s.strip()))  # 'hello     world'

# replace(" ", "") 的效果太強，會把所有空白都刪掉。
# 如果原本詞與詞之間應該保留一格，這種寫法就會把語意一起破壞掉。
print(repr(s.replace(" ", "")))  # 'helloworld'

# 如果你真正想做的是「壓縮多個空白成單一空白」，
# 更合理的做法是：先 strip() 去頭尾，再用 regex 把連續空白替換成一格。
print(repr(re.sub(r"\s+", " ", s.strip())))  # 'hello world'

# ── 生成器逐行清理（高效，不預載入記憶體）───────────
# 當資料很多時，逐行處理比先全部轉成新列表更省記憶體。
lines = ["  apple  \n", "  banana  \n"]

# (l.strip() for l in lines) 是生成器運算式，
# 每次迴圈只產生一個清理後的值，不會一次建立完整新列表。
for line in (l.strip() for l in lines):
    print(line)
