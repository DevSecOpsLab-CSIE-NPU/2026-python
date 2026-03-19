# R02. 正則表達式：搜尋、替換、旗標（2.4–2.8）
# re.compile / findall / sub / IGNORECASE / 非貪婪 / DOTALL
# 重點：先 compile 再重複使用，通常更清楚、也更有效率

import re

# ── 2.4 匹配和搜尋 ────────────────────────────────────
text = "Today is 11/27/2012. PyCon starts 3/13/2013."
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

# findall 會回傳所有匹配；因為有群組，所以每筆是 tuple
print(datepat.findall(text))
# [('11', '27', '2012'), ('3', '13', '2013')]

m = datepat.match("11/27/2012")
assert m is not None
# group(0) 是完整匹配；groups() 是各捕獲群組
print(m.group(0), m.groups())  # '11/27/2012' ('11', '27', '2012')

for m in datepat.finditer(text):
    # finditer 逐筆給 Match 物件，適合邊走訪邊處理
    month, day, year = m.groups()
    print(f"{year}-{month}-{day}")

# ── 2.5 搜尋和替換 ───────────────────────────────────
# 反向參照 \1 \2 \3 代表第 1~3 個捕獲群組
print(re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text))
# 'Today is 2012-11-27. PyCon starts 2013-3-13.'

# 命名群組
# 用命名群組可提升可讀性，特別適合複雜樣式
print(
    re.sub(
        r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)",
        r"\g<year>-\g<month>-\g<day>",
        text,
    )
)

# re.subn 回傳替換次數
newtext, n = re.subn(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)
print(f"替換了 {n} 次")  # 替換了 2 次

# ── 2.6 忽略大小寫 ───────────────────────────────────
s = "UPPER PYTHON, lower python, Mixed Python"
# IGNORECASE 讓大小寫不敏感，但回傳內容保留原字串大小寫
print(re.findall("python", s, flags=re.IGNORECASE))
# ['PYTHON', 'python', 'Python']

# ── 2.7 非貪婪（最短匹配）────────────────────────────
text2 = 'Computer says "no." Phone says "yes."'
# .* 會盡量吃到最後一個引號（貪婪）
print(re.compile(r'"(.*)"').findall(text2))  # 貪婪：['no." Phone says "yes.']
# .*? 會在第一個可結束的位置停下（非貪婪）
print(re.compile(r'"(.*?)"').findall(text2))  # 非貪婪：['no.', 'yes.']

# ── 2.8 多行匹配（DOTALL）────────────────────────────
code = "/* this is a\nmultiline comment */"
# DOTALL 讓 . 也能匹配換行符號
print(re.compile(r"/\*(.*?)\*/", re.DOTALL).findall(code))
# [' this is a\nmultiline comment ']
