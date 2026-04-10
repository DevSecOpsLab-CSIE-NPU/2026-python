# U01. 字串分割與匹配的陷阱（2.1–2.11）
# 說明：捕獲分組保留分隔符 / startswith 必須傳 tuple / strip 只處理頭尾

import re

# ─────────────────────────────────────────────────────────────────
# 捕獲分組保留分隔符（2.1）
# 說明：正則表達式中使用捕獲分組 () 可以讓分隔符被保留下來
# ─────────────────────────────────────────────────────────────────

# 原始字串，包含多種分隔符（空白、分號、逗號）
line = "asdf fjdk; afed, fjek,asdf, foo"

# 使用捕獲分組：正則表達式中的 (;|,|\s) 會保留分隔符
# 結果會是：['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo', '']
fields = re.split(r"(;|,|\s)\s*", line)

# fields[::2] 取偶數索引，取得實際的值（asdf, fjdk, afed, fjek, asdf, foo）
values = fields[::2]

# fields[1::2] 取奇數索引，取得分隔符，最後加一個空字串湊成對
delimiters = fields[1::2] + [""]

# 重建字串：將值和分隔符交替組合
rebuilt = "".join(v + d for v, d in zip(values, delimiters))
print(rebuilt)  # 輸出：'asdf fjdk;afed,fjek,asdf,foo'
# 注意：這裡保留了原始的分隔符（空白、分號、逗號）


# ─────────────────────────────────────────────────────────────────
# startswith 必須傳 tuple（2.2）
# 說明：startswith() 方法需要傳入 tuple 或 list，不能只傳 list
# ─────────────────────────────────────────────────────────────────

url = "http://www.python.org"

# 要檢查的前綴列表
choices = ["http:", "ftp:"]

try:
    # 嘗試直接傳入 list（會報錯！）
    url.startswith(choices)  # type: ignore[arg-type]
except TypeError as e:
    print(f"TypeError: {e}")  # 輸出：startswith first arg must be str or a tuple of str

# 正確做法：將 list 轉換為 tuple
print(url.startswith(tuple(choices)))  # 輸出：True


# ─────────────────────────────────────────────────────────────────
# strip 只處理頭尾，不處理中間（2.11）
# 說明：strip() 只會移除字串開頭和結尾的空白，中間的空白會保留
# ─────────────────────────────────────────────────────────────────

s = "  hello     world  "

# strip() 只移除頭尾空白，中間多餘空白還在
print(repr(s.strip()))  # 輸出：'hello     world'

# replace() 會移除所有空白，但連單字間的空白也沒了（可能過頭）
print(repr(s.replace(" ", "")))  # 輸出：'helloworld'

# 正確做法：先用 strip() 移除頭尾空白，再用正則表達式將中間多餘空白合併為一個
print(repr(re.sub(r"\s+", " ", s.strip())))  # 輸出：'hello world'


# ─────────────────────────────────────────────────────────────────
# 生成器逐行清理（高效，不預載入記憶體）
# 說明：使用生成器表達式可以節省記憶體，適合處理大檔案
# ─────────────────────────────────────────────────────────────────

lines = ["  apple  \n", "  banana  \n"]

# 使用生成器表達式，每次只處理一行，不會一次性載入所有資料
for line in (l.strip() for l in lines):
    print(line)
# 輸出：
# apple
# banana