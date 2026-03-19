# R03. 字串清理、對齊、拼接與格式化（2.11–2.16）
#
# 本檔示範重點：
# 1) strip/lstrip/rstrip 清理前後雜訊字元。
# 2) ljust/rjust/center/format 做欄位對齊。
# 3) join 做高效率字串拼接。
# 4) format / format_map / f-string 進行變數插值。
# 5) textwrap.fill 以指定寬度排版長段落。

import textwrap

# ── 2.11 清理字元 ─────────────────────────────────────
s = "  hello world \n"

# strip() 預設移除兩端空白字元（空格、\n、\t...），不影響中間內容
print(repr(s.strip()))  # 'hello world'

# lstrip() 只移除左側（前導）空白
print(repr(s.lstrip()))  # 'hello world \n'

# 也可指定要移除的「字元集合」；不是整段字串比對，而是兩端逐字剝除
print("-----hello=====".strip("-="))  # 'hello'

# ── 2.13 字串對齊 ─────────────────────────────────────
text = "Hello World"

# ljust/rjust/center 常用於表格或報表輸出
print(text.ljust(20))  # 'Hello World         '
print(text.rjust(20))  # '         Hello World'
print(text.center(20, "*"))  # '****Hello World*****'

# format 也能做同樣對齊：^ 置中、< 靠左、> 靠右
print(format(text, "^20"))  # '    Hello World     '

# 數字格式：>10.2f 代表右對齊、總寬 10、保留 2 位小數
print(format(1.2345, ">10.2f"))  # '      1.23'

# ── 2.14 合併拼接 ─────────────────────────────────────
parts = ["Is", "Chicago", "Not", "Chicago?"]

# join 是拼接多段字串的標準做法，通常比反覆 + 更有效率
print(" ".join(parts))  # 'Is Chicago Not Chicago?'
print(",".join(parts))  # 'Is,Chicago,Not,Chicago?'

data = ["ACME", 50, 91.1]

# join 只能接收字串，非字串需先轉型
print(",".join(str(d) for d in data))  # 'ACME,50,91.1'

# ── 2.15 插入變量 ─────────────────────────────────────
name, n = "Guido", 37
s = "{name} has {n} messages."

# format：明確傳入對應名稱
print(s.format(name=name, n=n))  # 'Guido has 37 messages.'

# format_map(vars())：直接用目前作用域變數字典做映射
print(s.format_map(vars()))  # 'Guido has 37 messages.'

# f-string：語法最精簡、可讀性高，日常最常用
print(f"{name} has {n} messages.")  # f-string（最簡潔）

# ── 2.16 指定列寬 ─────────────────────────────────────
long_s = (
    "Look into my eyes, look into my eyes, the eyes, "
    "not around the eyes, look into my eyes, you're under."
)

# fill(long_s, 40)：每行寬度約 40 字元，自動換行
print(textwrap.fill(long_s, 40))

# initial_indent：只在第一行加縮排
print(textwrap.fill(long_s, 40, initial_indent="    "))
