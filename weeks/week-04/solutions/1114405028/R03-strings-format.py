# R03. 字串清理、對齊、拼接與格式化（2.11–2.16）
# strip / ljust / join / format / format_map / textwrap

import textwrap

# ── 2.11 清理字元 ─────────────────────────────────────
s = "  hello world \n"
print(repr(s.strip()))  # 去除左右空白與換行，repr 可清楚看到隱藏字元差異
print(repr(s.lstrip()))  # 只去除左側空白，右側保留
print("-----hello=====".strip("-="))  # 指定可移除字元集合（左右兩端都會處理）

# ── 2.13 字串對齊 ─────────────────────────────────────
text = "Hello World"
print(text.ljust(20))  # 左對齊，總寬 20，不足補空白
print(text.rjust(20))  # 右對齊
print(text.center(20, "*"))  # 置中，使用 * 當填充字元
print(format(text, "^20"))  # format 規格：^ 代表置中
print(format(1.2345, ">10.2f"))  # 數值右對齊，寬 10，小數 2 位

# ── 2.14 合併拼接 ─────────────────────────────────────
parts = ["Is", "Chicago", "Not", "Chicago?"]
print(" ".join(parts))  # 用空白連接字串序列
print(",".join(parts))  # 用逗號連接（CSV 常見）

data = ["ACME", 50, 91.1]
print(",".join(str(d) for d in data))  # join 只能接收字串，需先將數字轉字串

# ── 2.15 插入變量 ─────────────────────────────────────
name, n = "Guido", 37
s = "{name} has {n} messages."
print(s.format(name=name, n=n))  # 以關鍵字參數填入欄位
print(s.format_map(vars()))  # vars() 取目前區域變數 dict，直接映射到模板
print(f"{name} has {n} messages.")  # f-string：語法最直覺、效能也通常較佳

# ── 2.16 指定列寬 ─────────────────────────────────────
long_s = (
    "Look into my eyes, look into my eyes, the eyes, "
    "not around the eyes, look into my eyes, you're under."
)
print(textwrap.fill(long_s, 40))
print(textwrap.fill(long_s, 40, initial_indent="    "))  # 只設定第一行縮排（段首縮排）
