import re

# ── 陷阱 1：捕獲分組會保留分隔符（2.1） ─────────────────────────
# 當使用 re.split 時，若正則表達式包含「捕獲括號 ()」，分隔符也會被傳回。
line = "asdf fjdk; afed, fjek,asdf, foo"

# 正則解釋：(;|,|\s) 匹配分號、逗號或空白；\s* 匹配隨後的任意空白
# 因為使用了括號，結果會包含：[內容, 分隔符, 內容, 分隔符...]
fields = re.split(r"(;|,|\s)\s*", line)

# 利用切片步長 (Slicing step) 分離內容與分隔符
values = fields[::2]       # 偶數索引：得到的是實際的文字內容
delimiters = fields[1::2] + [""]  # 奇數索引：得到分隔符，最後補一個空字串方便對齊

# 重新組合：這在需要「修改文字但保留原始分隔結構」時非常有用
rebuilt = "".join(v + d for v, d in zip(values, delimiters))
print(rebuilt)  # 輸出: 'asdf fjdk;afed,fjek,asdf,foo'


# ── 陷阱 2：startswith/endswith 必須傳入 tuple（2.2） ───────────
url = "http://www.python.org"
choices = ["http:", "ftp:"]

try:
    # 錯誤示範：startswith 不接受 list 作為參數
    url.startswith(choices)  
except TypeError as e:
    print(f"TypeError: {e}")  # 拋出錯誤：must be str or tuple, not list

# 正確做法：必須明確轉換成 tuple
print(url.startswith(tuple(choices)))  # 輸出: True


# ── 陷阱 3：strip 家族只處理頭尾，不碰中間（2.11） ──────────────
s = "  hello     world  "

# strip() 只會移除字串「最左邊」與「最右邊」的空白
print(repr(s.strip()))  # 輸出: 'hello     world' (中間的連續空白依然存在)

# replace(" ", "") 會移除「所有」空白，通常這不是我們要的 (單字會黏在一起)
print(repr(s.replace(" ", "")))  # 輸出: 'helloworld'

# 正確清理中間多餘空白的方法：先 strip 頭尾，再用 re.sub 將多個空白替換為單一空白
print(repr(re.sub(r"\s+", " ", s.strip())))  # 輸出: 'hello world'


# ── 進階技巧：生成器表達式（Generator Expression）逐行清理 ────────
# 當處理大型檔案（如數 GB 的 Log）時，不應一次將整個檔案讀入記憶體
lines = ["  apple  \n", "  banana  \n"]

# 使用生成器 ( ) 而非列表推導 [ ]，可以達到「延遲求值」，節省記憶體
cleaned_lines = (l.strip() for l in lines)

for line in cleaned_lines:
    print(line)  # 逐行輸出清理後的結果：'apple', 'banana'