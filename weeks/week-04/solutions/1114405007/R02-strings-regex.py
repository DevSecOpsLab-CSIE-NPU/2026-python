# R02. 正則表達式：搜尋、替換、旗標（2.4–2.8）
# 這份範例集中展示正則表達式最常見的幾種用途：
# 1. 從文字中找出符合規則的資料
# 2. 把符合規則的內容重新排列後替換
# 3. 控制大小寫、跨行與最短匹配等行為

import re

# ── 2.4 匹配和搜尋 ────────────────────────────────────
# 這是一段包含兩個日期的文字。
# 等一下會用正則表達式把月/日/年拆出來。
text = "Today is 11/27/2012. PyCon starts 3/13/2013."

# (\d+) 表示「一個以上的數字」。
# 用三組括號包起來，代表要分別捕獲 month/day/year 三段資料。
# compile() 可以先把規則建立好，之後重複使用時較方便。
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

# findall() 會找出字串中所有符合規則的內容。
# 因為有三個捕獲群組，所以結果會是一個個 tuple。
print(datepat.findall(text))
# [('11', '27', '2012'), ('3', '13', '2013')]

# match() 只會從字串開頭開始比對。
# 這裡剛好字串本身就是日期，所以會成功。
# 如果開頭不是日期，就會得到 None。
m = datepat.match("11/27/2012")
assert m is not None

# group(0) 是整段符合的文字。
# groups() 則會回傳所有括號捕獲到的內容。
print(m.group(0), m.groups())  # '11/27/2012' ('11', '27', '2012')

# finditer() 會回傳一個可迭代的 Match 物件序列。
# 好處是每次都能取得完整 match 物件，適合逐筆處理。
for m in datepat.finditer(text):
    month, day, year = m.groups()
    print(f"{year}-{month}-{day}")

# ── 2.5 搜尋和替換 ───────────────────────────────────
# sub() 可以把符合正則規則的內容直接取代掉。
# \1、\2、\3 分別代表第 1、2、3 個捕獲群組。
# 這裡是把 mm/dd/yyyy 重新排成 yyyy-mm-dd。
print(re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text))
# 'Today is 2012-11-27. PyCon starts 2013-3-13.'

# 命名群組的好處是可讀性更高。
# 當群組很多時，用名稱 month/day/year 會比 \1 \2 \3 更不容易搞混。
print(
    re.sub(
        r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)",
        r"\g<year>-\g<month>-\g<day>",
        text,
    )
)

# subn() 會同時回傳：
# 1. 替換後的新字串
# 2. 一共替換了幾次
# 如果你想知道資料到底改了多少處，這個方法很實用。
newtext, n = re.subn(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)
print(f"替換了 {n} 次")  # 替換了 2 次

# ── 2.6 忽略大小寫 ───────────────────────────────────
# IGNORECASE 讓 Python 在比對時忽略英文字母大小寫差異。
# 所以 PYTHON、python、Python 都能被找出來。
s = "UPPER PYTHON, lower python, Mixed Python"
print(re.findall("python", s, flags=re.IGNORECASE))
# ['PYTHON', 'python', 'Python']

# ── 2.7 非貪婪（最短匹配）────────────────────────────
# 這個字串裡面有兩段被雙引號包住的內容。
text2 = 'Computer says "no." Phone says "yes."'

# .* 是貪婪匹配，意思是會盡可能吃到最長。
# 因此它會從第一個雙引號一路吃到最後一個雙引號。
print(re.compile(r'"(.*)"').findall(text2))  # 貪婪：['no." Phone says "yes.']

# .*? 是非貪婪匹配，意思是「夠用就好」。
# 所以它會各自抓到最短的一段：no. 與 yes.
print(re.compile(r'"(.*?)"').findall(text2))  # 非貪婪：['no.', 'yes.']

# ── 2.8 多行匹配（DOTALL）────────────────────────────
# 一般情況下，. 不會匹配換行字元。
# 加上 re.DOTALL 後，. 才能跨行匹配。
# 這對於處理多行註解、區塊文字、HTML 片段很常見。
code = "/* this is a\nmultiline comment */"
print(re.compile(r"/\*(.*?)\*/", re.DOTALL).findall(code))
# [' this is a\nmultiline comment ']
