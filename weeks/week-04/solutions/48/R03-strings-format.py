# R03. 字串清理、對齊、拼接與格式化（2.11–2.16）
# strip / ljust / join / format / format_map / textwrap
# 重點：這些是日常資料清理與輸出排版最常用的字串技巧

import textwrap

# ── 2.11 清理字元 ─────────────────────────────────────
s = "  hello world \n"
# strip() 預設移除前後空白（含空格、換行、tab）
print(repr(s.strip()))  # 'hello world'
print(repr(s.lstrip()))  # 'hello world \n'
# 可指定要移除的字元集合（不是子字串）
print("-----hello=====".strip("-="))  # 'hello'

# ── 2.13 字串對齊 ─────────────────────────────────────
text = "Hello World"
# ljust / rjust / center 常用於表格輸出
print(text.ljust(20))  # 'Hello World         '
print(text.rjust(20))  # '         Hello World'
print(text.center(20, "*"))  # '****Hello World*****'
# format 可統一處理字串與數字的對齊、寬度、小數位
print(format(text, "^20"))  # '    Hello World     '
print(format(1.2345, ">10.2f"))  # '      1.23'

# ── 2.14 合併拼接 ─────────────────────────────────────
parts = ["Is", "Chicago", "Not", "Chicago?"]
# join 比連續 + 串接更有效率，特別在大量字串時
print(" ".join(parts))  # 'Is Chicago Not Chicago?'
print(",".join(parts))  # 'Is,Chicago,Not,Chicago?'

data = ["ACME", 50, 91.1]
# join 需要字串元素，其他型別先轉 str
print(",".join(str(d) for d in data))  # 'ACME,50,91.1'

# ── 2.15 插入變量 ─────────────────────────────────────
name, n = "Guido", 37
s = "{name} has {n} messages."
# format_map(vars()) 會直接從目前作用域抓同名變數
print(s.format(name=name, n=n))  # 'Guido has 37 messages.'
print(s.format_map(vars()))  # 'Guido has 37 messages.'
print(f"{name} has {n} messages.")  # f-string（最簡潔）

# ── 2.16 指定列寬 ─────────────────────────────────────
long_s = (
    "Look into my eyes, look into my eyes, the eyes, "
    "not around the eyes, look into my eyes, you're under."
)
# textwrap.fill 會自動在指定寬度換行，適合 CLI 輸出或文件排版
print(textwrap.fill(long_s, 40))
# initial_indent 只影響第一行縮排
print(textwrap.fill(long_s, 40, initial_indent="    "))
