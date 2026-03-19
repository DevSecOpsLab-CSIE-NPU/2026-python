# R02. 正則表達式：搜尋、替換、旗標（2.4–2.8）
# re.compile / findall / sub / IGNORECASE / 非貪婪 / DOTALL
"""
本範例展示 Python re 模組常見的使用模式：
 1) 建立正則表達式物件（re.compile）並反覆使用
 2) 搜尋（match / search / findall / finditer）與擷取群組
 3) 取代（re.sub / re.subn）與命名群組
 4) 忽略大小寫（re.IGNORECASE）
 5) 非貪婪匹配（最短匹配）與貪婪匹配的差異
 6) DOTALL 讓點號 (.) 能匹配換行符號

這些技巧是處理日誌、資料清理、字串解析的基礎。
"""

import re

# ── 2.4 匹配和搜尋 ────────────────────────────────────
# re.compile 可以把正則模式編譯成可以重複使用的 Pattern 物件，
# 在需要多次執行同一模式時可以提升效能。
text = "Today is 11/27/2012. PyCon starts 3/13/2013."

# (
#   \d+  : 一個或多個數字
#   /     : 字元 /
# )
# 這裡有三個群組，分別對應月、日、年。
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

# findall 會找出所有符合的子串，並回傳清單，
# 每個元素是群組所組成的 tuple（這裡每一筆是 (month, day, year)）。
print(datepat.findall(text))
# [('11', '27', '2012'), ('3', '13', '2013')]

# match 只從字串開頭嘗試匹配（不會掃描整個字串）
m = datepat.match("11/27/2012")
assert m is not None
print(m.group(0), m.groups())  # '11/27/2012' ('11', '27', '2012')

# finditer 會回傳 iterator，每一個迭代項目都是 Match 物件
# 比較適合需要逐一處理每個匹配結果的情境。
for m in datepat.finditer(text):
    month, day, year = m.groups()
    print(f"{year}-{month}-{day}")

# ── 2.5 搜尋和替換 ───────────────────────────────────
# re.sub 用正則替換字串，回傳新的字串。
# r"\3-\1-\2" 中的 \1 \2 \3 分別表示第一、二、三個群組。
print(re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text))
# 'Today is 2012-11-27. PyCon starts 2013-3-13.'

# 命名群組：用 (?P<name>...) 指定群組名稱，替換時可以用 \g<name>。
print(
    re.sub(
        r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)",
        r"\g<year>-\g<month>-\g<day>",
        text,
    )
)

# re.subn 會回傳 (new_string, 替換次數)，方便計數或檢查是否有替換。
newtext, n = re.subn(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)
print(f"替換了 {n} 次")  # 替換了 2 次

# ── 2.6 忽略大小寫 ───────────────────────────────────
# flag 可以傳給 re.findall、re.search 等；也可以在 compile 時指定。
s = "UPPER PYTHON, lower python, Mixed Python"
print(re.findall("python", s, flags=re.IGNORECASE))
# ['PYTHON', 'python', 'Python']

# ── 2.7 非貪婪（最短匹配）────────────────────────────
# 默認 .* 是「貪婪」的，會匹配最長的可能字串。
# 在某些情境下，我們希望匹配最短的那一段，此時使用 .*?
text2 = 'Computer says "no." Phone says "yes."'
print(re.compile(r'"(.*)"').findall(text2))  # 貪婪：['no." Phone says "yes.']
print(re.compile(r'"(.*?)"').findall(text2))  # 非貪婪：['no.', 'yes.']

# ── 2.8 多行匹配（DOTALL）────────────────────────────
# 預設情況下 '.' 不會匹配換行符號，要讓 '.' 匹配換行須使用 re.DOTALL。
code = "/* this is a\nmultiline comment */"
print(re.compile(r"/\*(.*?)\*/", re.DOTALL).findall(code))
# [' this is a\nmultiline comment ']
