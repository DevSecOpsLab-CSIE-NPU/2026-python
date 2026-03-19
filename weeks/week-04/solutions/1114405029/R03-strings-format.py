# R03. 字串清理、對齊、拼接與格式化（2.11–2.16）
# 主題包含：
# strip / ljust / join / format / format_map / textwrap

import textwrap

# ── 2.11 清理字元 ─────────────────────────────────────

# 建立一個字串 s
# 前後包含空白與換行字元
s = "  hello world \n"

# strip()：移除字串前後的空白（包含空格、\n、\t）
print("使用 strip() 去除前後空白：")
print(repr(s.strip()))  # 'hello world'

# lstrip()：只移除左邊（開頭）的空白
print("使用 lstrip() 去除左邊空白：")
print(repr(s.lstrip()))  # 'hello world \n'

# strip("-=")：可指定要移除的字元（只移除前後，不影響中間）
print("指定移除 '-' 和 '=' 字元：")
print("-----hello=====".strip("-="))  # 'hello'

print()  # 空行

# ── 2.13 字串對齊 ─────────────────────────────────────

text = "Hello World"

# ljust(寬度)：左對齊，右邊補空白
print("左對齊（ljust）：")
print(repr(text.ljust(20)))  # 'Hello World         '

# rjust(寬度)：右對齊，左邊補空白
print("右對齊（rjust）：")
print(repr(text.rjust(20)))  # '         Hello World'

# center(寬度, 填充字元)：置中
print("置中（center）：")
print(repr(text.center(20, "*")))  # '****Hello World*****'

# 使用 format() 也可以做對齊
print("使用 format() 置中：")
print(repr(format(text, "^20")))  # '    Hello World     '

# 格式化數字（寬度10，小數2位，右對齊）
print("數字格式化（寬度+小數）：")
print(repr(format(1.2345, ">10.2f")))  # '      1.23'

print()  # 空行

# ── 2.14 合併拼接 ─────────────────────────────────────

parts = ["Is", "Chicago", "Not", "Chicago?"]

# 使用 join() 以空白連接
print("使用空白 join：")
print(" ".join(parts))  # 'Is Chicago Not Chicago?'

# 使用逗號連接
print("使用逗號 join：")
print(",".join(parts))  # 'Is,Chicago,Not,Chicago?'

# 若資料包含非字串（例如數字），需先轉型
data = ["ACME", 50, 91.1]

print("混合型資料 join（需轉字串）：")
print(",".join(str(d) for d in data))  # 'ACME,50,91.1'

print()  # 空行

# ── 2.15 插入變量 ─────────────────────────────────────

name, n = "Guido", 37

# 使用 format() 插入變數
s = "{name} has {n} messages."
print("使用 format()：")
print(s.format(name=name, n=n))  # 'Guido has 37 messages.'

# 使用 format_map() 搭配 vars()
# vars() 會回傳目前區域變數的 dict
print("使用 format_map(vars())：")
print(s.format_map(vars()))  # 'Guido has 37 messages.'

# 使用 f-string（最簡潔、現代寫法）
print("使用 f-string：")
print(f"{name} has {n} messages.")

print()  # 空行

# ── 2.16 指定列寬（自動換行）─────────────────────────

# 建立一段很長的字串
long_s = (
    "Look into my eyes, look into my eyes, the eyes, "
    "not around the eyes, look into my eyes, you're under."
)

# textwrap.fill()：將長字串依指定寬度自動換行
print("指定每行寬度 40：")
print(textwrap.fill(long_s, 40))

print()  # 空行

# initial_indent：第一行縮排
print("第一行縮排（initial_indent）：")
print(textwrap.fill(long_s, 40, initial_indent="    "))