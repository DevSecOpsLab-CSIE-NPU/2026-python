# R02. 正則表達式：搜尋、替換、旗標（2.4–2.8）
# re.compile / findall / sub / IGNORECASE / 非貪婪 / DOTALL

import re

# ── 2.4 匹配和搜尋 ────────────────────────────────────
# 測試字串：包含兩個日期，格式為 月/日/年。
text = "Today is 11/27/2012. PyCon starts 3/13/2013."

# 建立正則模式（建議做法）：
# - re.compile 可重複使用同一模式，效能與可讀性通常較好。
# - (\d+) 代表「一個以上數字」，使用括號表示捕獲群組。
# - 共有三個群組：month/day/year。
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

# findall：找出所有匹配，回傳 list。
# 因為模式含群組，所以每筆結果是 tuple（對應各群組）。
print(datepat.findall(text))
# [('11', '27', '2012'), ('3', '13', '2013')]

# match：只從字串「開頭」開始匹配。
# 這裡 '11/27/2012' 開頭就符合，因此 m 不是 None。
m = datepat.match("11/27/2012")
assert m is not None

# group(0) 是整段匹配字串；groups() 是各捕獲群組 tuple。
print(m.group(0), m.groups())  # '11/27/2012' ('11', '27', '2012')

# finditer：逐筆回傳 match 物件（iterator）。
# 適合需要更多 match 細節（位置、群組）時使用。
for m in datepat.finditer(text):
    month, day, year = m.groups()
    # 重新格式化成 YYYY-MM-DD（示範字串重組）
    print(f"{year}-{month}-{day}")

# ── 2.5 搜尋和替換 ───────────────────────────────────
# sub：用反向參照（\1, \2, \3）做群組替換。
# 這裡把 M/D/Y 改成 Y-M-D。
print(re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text))
# 'Today is 2012-11-27. PyCon starts 2013-3-13.'

# 命名群組：可提升可讀性，避免記 \1、\2、\3 容易混淆。
# (?P<name>...) 定義命名群組，\g<name> 在替換字串中引用。
print(
    re.sub(
        r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)",
        r"\g<year>-\g<month>-\g<day>",
        text,
    )
)

# re.subn：同時回傳 (新字串, 替換次數)
# 適合需要確認實際替換量的情境（例如資料清洗驗證）。
newtext, n = re.subn(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)
print(f"替換了 {n} 次")  # 替換了 2 次

# ── 2.6 忽略大小寫 ───────────────────────────────────
s = "UPPER PYTHON, lower python, Mixed Python"

# IGNORECASE 讓大小寫不敏感：Python / PYTHON / python 都能匹配。
print(re.findall("python", s, flags=re.IGNORECASE))
# ['PYTHON', 'python', 'Python']

# ── 2.7 非貪婪（最短匹配）────────────────────────────
text2 = 'Computer says "no." Phone says "yes."'

# 貪婪匹配 .* ：會盡可能吃到最長結果，
# 因此從第一個引號一路吃到最後一個引號。
print(re.compile(r'"(.*)"').findall(text2))  # 貪婪：['no." Phone says "yes.']

# 非貪婪 .*? ：會用最短長度滿足條件，
# 因此得到每一對引號內的獨立內容。
print(re.compile(r'"(.*?)"').findall(text2))  # 非貪婪：['no.', 'yes.']

# ── 2.8 多行匹配（DOTALL）────────────────────────────
code = "/* this is a\nmultiline comment */"

# 預設下，. 不匹配換行字元；加上 re.DOTALL 後才會跨行匹配。
# 這裡可正確抓到 C 風格多行註解內容。
print(re.compile(r"/\*(.*?)\*/", re.DOTALL).findall(code))
# [' this is a\nmultiline comment ']
