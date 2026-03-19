# 詳細註解：本檔示範字串清理、對齊與格式化策略。
# 重點：`join`、`format`、`format_map` 各有適用情境。
# 用途：輸出報表、組字串、處理使用者輸入。
# 注意：格式化前先做 `strip` 等清理可降低錯誤。
# R03. 字串清理、對齊、拼接與格式化（2.11–2.16）
# strip / ljust / join / format / format_map / textwrap

import textwrap

# ── 2.11 清理字元 ─────────────────────────────────────
s = "  hello world \n"
print(repr(s.strip()))  # 'hello world'
print(repr(s.lstrip()))  # 'hello world \n'
print("-----hello=====".strip("-="))  # 'hello'

# ── 2.13 字串對齊 ─────────────────────────────────────
text = "Hello World"
print(text.ljust(20))  # 'Hello World         '
print(text.rjust(20))  # '         Hello World'
print(text.center(20, "*"))  # '****Hello World*****'
print(format(text, "^20"))  # '    Hello World     '
print(format(1.2345, ">10.2f"))  # '      1.23'

# ── 2.14 合併拼接 ─────────────────────────────────────
parts = ["Is", "Chicago", "Not", "Chicago?"]
print(" ".join(parts))  # 'Is Chicago Not Chicago?'
print(",".join(parts))  # 'Is,Chicago,Not,Chicago?'

data = ["ACME", 50, 91.1]
print(",".join(str(d) for d in data))  # 'ACME,50,91.1'

# ── 2.15 插入變量 ─────────────────────────────────────
name, n = "Guido", 37
s = "{name} has {n} messages."
print(s.format(name=name, n=n))  # 'Guido has 37 messages.'
print(s.format_map(vars()))  # 'Guido has 37 messages.'
print(f"{name} has {n} messages.")  # f-string（最簡潔）

# ── 2.16 指定列寬 ─────────────────────────────────────
long_s = (
    "Look into my eyes, look into my eyes, the eyes, "
    "not around the eyes, look into my eyes, you're under."
)
print(textwrap.fill(long_s, 40))
print(textwrap.fill(long_s, 40, initial_indent="    "))
