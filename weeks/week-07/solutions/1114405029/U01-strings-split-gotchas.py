# U01. 字串分割與匹配的陷阱（2.1–2.11）
# 捕獲分組保留分隔符 / startswith 必須傳 tuple / strip 只處理頭尾

import re

# ── 捕獲分組保留分隔符（2.1）─────────────────────────
# 使用 re.split 時，若正則表達式包含括號 ( )，則分隔符也會被保留在結果清單中
line = "asdf fjdk; afed, fjek,asdf, foo"
fields = re.split(r"(;|,|\s)\s*", line)
values = fields[::2]  # 取得偶數索引位：實際的文字內容
delimiters = fields[1::2] + [""] # 取得奇數索引位：分隔符號，末尾補空字串以利對齊
# 重新組合字串，將文字與其後的分隔符交替拼回
rebuilt = "".join(v + d for v, d in zip(values, delimiters))
print(rebuilt)  # 'asdf fjdk;afed,fjek,asdf,foo'

# ── startswith 必須傳 tuple（2.2）────────────────────
url = "http://www.python.org"
choices = ["http:", "ftp:"]
try:
    # 錯誤示範：startswith/endswith 不接受 list 作為多個選項的參數
    url.startswith(choices)  # type: ignore[arg-type]
except TypeError as e:
    print(f"TypeError: {e}")  # 輸出錯誤訊息：不能傳 list！
# 正確做法：必須先將 list 轉換為 tuple
print(url.startswith(tuple(choices)))  # True

# ── strip 只處理頭尾，不處理中間（2.11）──────────────
s = "  hello     world  "
print(repr(s.strip()))  # 'hello     world'（僅移除頭尾空白，中間的多餘空白依然存在）
print(repr(s.replace(" ", "")))  # 'helloworld'（全部移除，導致單字連在一起）
# 最佳實踐：先用 strip 處理頭尾，再用 re.sub 將中間多個連續空白替換為單一空白
print(repr(re.sub(r"\s+", " ", s.strip())))  # 'hello world'

# 生成器逐行清理：使用產生器表達式 (generator expression) 處理大型資料庫或檔案，節省記憶體
lines = ["  apple  \n", "  banana  \n"]
for line in (l.strip() for l in lines):
    print(line)