# R03. 字串清理、對齊與拼接（範例 2.11–2.16）
import textwrap

# ── 2.11 清理字元 ──
s = "  hello world \n"
print(repr(s.strip()))  # 清除兩端空白與換行：'hello world'
print("-----hello=====".strip("-="))  # 指定清除字元：'hello'

# ── 2.13 字串對齊 ──
text = "Hello World"
print(text.ljust(20))       # 左對齊，總長 20
print(text.center(20, "*")) # 居中，空白處填滿 *
print(format(1.2345, ">10.2f")) # 數字格式化：右對齊、長度 10、小數 2 位

# ── 2.14 合併拼接 ──
parts = ["Is", "Chicago", "Not", "Chicago?"]
# 建議：合併大量字串時使用 join，效能優於用 + 號不斷相加
print(" ".join(parts)) 

# ── 2.16 指定寬度換行 ──
s = "Look into my eyes, look into my eyes, the eyes, the eyes..."
print(textwrap.fill(s, 40)) # 每 40 個字元自動插入換行符