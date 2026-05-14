# R05. 資料統計與累加（6.13）
# Counter / defaultdict / namedtuple 整合應用

# 匯入collections模組中的實用類別
from collections import Counter, defaultdict, namedtuple

# ── Counter：計數器 ──────────────────────────────────────
# 定義一個包含重複元素的列表
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# 使用Counter建立計數器，自動統計每個元素的出現次數
cnt = Counter(words)
print("Counter：", cnt)  # 輸出計數結果

# 使用most_common()取得出現次數最多的元素
print("最多出現：", cnt.most_common(2))      # 取得前2名最多的元素

# Counter物件可以直接相加合併統計結果
extra = Counter(["banana", "cherry"])  # 額外的計數器
print("合併：", cnt + extra)  # 輸出合併後的結果

# ── defaultdict：有預設值的 dict ─────────────────────────
# 定義一個包含系別和姓名的記錄列表
records = [
    ("系資", "Alice"),
    ("電子", "Bob"),
    ("系資", "Carol"),
    ("電子", "David"),
    ("系資", "Eve"),
]

# 使用defaultdict(list)建立預設值為空列表的字典
# 這樣在存取不存在的鍵時會自動建立空列表
by_dept = defaultdict(list)
for dept, name in records:
    by_dept[dept].append(name)  # 將姓名加入對應系別的列表

print("\ndefaultdict：")
for dept, members in by_dept.items():
    print(f"  {dept}: {members}")  # 輸出每個系別的成員列表

# defaultdict(int)用於計數
score_sum = defaultdict(int)  # 預設值為0的字典
scores = [("Alice", 90), ("Bob", 80), ("Alice", 85), ("Bob", 70)]
for name, score in scores:
    score_sum[name] += score  # 累加每個人的分數
print("\n各人總分：", dict(score_sum))  # 輸出每個人的總分

# ── namedtuple：具名結構，更可讀 ─────────────────────────
# 使用namedtuple建立具名元組，提供更好的可讀性和存取方式
Stock = namedtuple("Stock", ["symbol", "price", "change"])  # 定義Stock具名元組
s = Stock("AA", 39.48, -0.18)  # 建立Stock實例
print(f"\n{s.symbol}: ${s.price}  漲跌 {s.change}")  # 使用屬性名稱存取值

# ── 綜合：從 list of dict 做統計 ─────────────────────────
# 定義包含系別和分數的字典列表
data = [
    {"dept": "系資", "score": 85},
    {"dept": "電子", "score": 78},
    {"dept": "系資", "score": 92},
    {"dept": "電子", "score": 88},
]

# 使用defaultdict(list)按系別分組分數
dept_scores = defaultdict(list)
for row in data:
    dept_scores[row["dept"]].append(row["score"])  # 將分數加入對應系別

print("\n各系平均：")
for dept, scores in dept_scores.items():
    avg = sum(scores) / len(scores)  # 計算平均分數
    print(f"  {dept}: {avg:.1f}")  # 輸出系別和平均分數
