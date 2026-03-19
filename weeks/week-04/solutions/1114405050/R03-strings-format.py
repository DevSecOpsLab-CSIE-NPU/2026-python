# R03. 字串清理、對齊、拼接與格式化（2.11–2.16）
# strip / ljust / join / format / format_map / textwrap
"""
本檔範例示範常用的字串處理技巧：
 1) 字串清理（去除前後空白或指定字元）
 2) 字串對齊（左/右/置中對齊、指定寬度）
 3) 合併與拼接（join）
 4) 插入變量（format / format_map / f-string）
 5) 文字換行與指定列寬（textwrap）

這些用法在處理輸出報表、產生 log、格式化表格時非常實用。
"""

import textwrap

# ── 2.11 清理字元 ─────────────────────────────────────
# strip()    : 去掉字串開頭與結尾的空白（預設）或指定字元
# lstrip()   : 去掉左側（開頭）的空白或指定字元
# rstrip()   : 去掉右側（結尾）的空白或指定字元
s = "  hello world \n"
print(repr(s.strip()))  # 'hello world'
print(repr(s.lstrip()))  # 'hello world \n'

# strip() 也能指定要去掉的字元集合（與 regex 不同，會逐一比對）
print("-----hello=====".strip("-="))  # 'hello'

# ── 2.13 字串對齊 ─────────────────────────────────────
# ljust/rjust/center 會根據指定寬度補齊空白（預設）或指定字元
text = "Hello World"
print(text.ljust(20))  # 'Hello World         '
print(text.rjust(20))  # '         Hello World'
print(text.center(20, "*"))  # '****Hello World*****'

# format() 同樣可以用來指定對齊與格式化，語法與 f-string 類似
print(format(text, "^20"))  # '^' 表示置中
print(format(1.2345, ">10.2f"))  # '>' 置右 10 寬度，.2f 代表小數 2 位

# ── 2.14 合併拼接 ─────────────────────────────────────
# join() 將一系列字串用指定連接符串起來，是最常用的拼接方式
parts = ["Is", "Chicago", "Not", "Chicago?"]
print(" ".join(parts))  # 'Is Chicago Not Chicago?'
print(",".join(parts))  # 'Is,Chicago,Not,Chicago?'

# 如果資料中有非字串元素，需要先轉成字串
data = ["ACME", 50, 91.1]
print(",".join(str(d) for d in data))  # 'ACME,50,91.1'

# ── 2.15 插入變量 ─────────────────────────────────────
# format(): 使用大括號標記，並在 format() 裡傳入對應參數
name, n = "Guido", 37
s = "{name} has {n} messages."
print(s.format(name=name, n=n))  # 'Guido has 37 messages.'

# format_map(): 可以傳入 dict 或 vars() 來替換變量
print(s.format_map(vars()))  # 'Guido has 37 messages.'

# f-string：Python 3.6 之後最簡潔的字串格式化方式
print(f"{name} has {n} messages.")  # f-string（最簡潔）

# ── 2.16 指定列寬 ─────────────────────────────────────
# textwrap.fill 可以依指定寬度自動換行，比手動切割更方便
long_s = (
    "Look into my eyes, look into my eyes, the eyes, "
    "not around the eyes, look into my eyes, you're under."
)
print(textwrap.fill(long_s, 40))

# initial_indent 可以在第一行加上起始縮排，而其他行不受影響
print(textwrap.fill(long_s, 40, initial_indent="    "))
