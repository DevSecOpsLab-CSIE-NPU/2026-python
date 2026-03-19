# R02. 正則表達式：搜尋、替換、旗標（2.4–2.8）
#
# 本檔示範重點：
# 1) 先用 re.compile 建立可重用的模式物件。
# 2) 比較 findall / match / finditer 的差異。
# 3) 用 sub / subn 做批次替換與替換計數。
# 4) 了解 IGNORECASE、非貪婪 *?、DOTALL 的實際效果。

import re

# ── 2.4 匹配和搜尋 ────────────────────────────────────
text = "Today is 11/27/2012. PyCon starts 3/13/2013."

# (\d+)/(\d+)/(\d+)：
# - \d+ 代表一段以上數字
# - 三組括號分別捕獲 month/day/year，後續可用 groups() 取出
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

# findall 會掃過整個字串，回傳所有匹配（因有群組，結果是 tuple 清單）
print(datepat.findall(text))
# [('11', '27', '2012'), ('3', '13', '2013')]

# match 只會從字串「開頭位置」嘗試匹配
m = datepat.match("11/27/2012")
assert m is not None
# group(0) 是完整匹配；groups() 是各捕獲群組
print(m.group(0), m.groups())  # '11/27/2012' ('11', '27', '2012')

# finditer 回傳 iterator，每次給一個 Match 物件，適合逐筆處理
for m in datepat.finditer(text):
    month, day, year = m.groups()
    print(f"{year}-{month}-{day}")

# ── 2.5 搜尋和替換 ───────────────────────────────────
# sub 的替換字串可用 \1\2\3 參照捕獲群組（此處改成 year-month-day）
print(re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text))
# 'Today is 2012-11-27. PyCon starts 2013-3-13.'

# 命名群組：可讀性更好，尤其群組很多時不易搞混
print(
    re.sub(
        r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)",
        r"\g<year>-\g<month>-\g<day>",
        text,
    )
)

# re.subn：除了新字串，也會回傳替換次數
newtext, n = re.subn(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)
print(f"替換了 {n} 次")  # 替換了 2 次

# ── 2.6 忽略大小寫 ───────────────────────────────────
s = "UPPER PYTHON, lower python, Mixed Python"
# IGNORECASE 讓大小寫視為等價，能一次抓到所有 python 變體
print(re.findall("python", s, flags=re.IGNORECASE))
# ['PYTHON', 'python', 'Python']

# ── 2.7 非貪婪（最短匹配）────────────────────────────
text2 = 'Computer says "no." Phone says "yes."'
# .* 是貪婪量詞：會盡可能吃到最後一個引號
print(re.compile(r'"(.*)"').findall(text2))  # 貪婪：['no." Phone says "yes.']
# .*? 是非貪婪量詞：找到最短可成立匹配就停
print(re.compile(r'"(.*?)"').findall(text2))  # 非貪婪：['no.', 'yes.']

# ── 2.8 多行匹配（DOTALL）────────────────────────────
code = "/* this is a\nmultiline comment */"
# DOTALL 讓 . 也能匹配換行符，才能一次抓到跨行註解內容
print(re.compile(r"/\*(.*?)\*/", re.DOTALL).findall(code))
# [' this is a\nmultiline comment ']
