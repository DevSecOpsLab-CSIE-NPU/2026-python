"""
R05. 資料統計與累加（6.13）

本範例示範三個在資料處理中非常常見的工具：
    1. Counter - 用來統計元素出現次數
    2. defaultdict - 用來建立「有預設值」的字典，方便分組與累加
    3. namedtuple - 用來建立具名欄位的輕量資料結構

這些工具常被用在文字統計、資料清洗、報表彙總與簡單資料建模。
"""

from collections import Counter, defaultdict, namedtuple

# ── Counter：計數器 ──────────────────────────────────────
# Counter 會自動統計序列中每個元素出現的次數，回傳一個類似 dict 的物件。
# 這比手動建立 dict 再一個個累加更簡潔，也更不容易出錯。
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
cnt = Counter(words)
print("Counter：", cnt)

# most_common(n) 會回傳出現次數最多的前 n 個元素，格式是 [(元素, 次數), ...]
# 常用於找出熱門關鍵字、最常出現的商品、最高頻的事件等。
print("最多出現：", cnt.most_common(2))      # [('apple', 3), ('banana', 2)]

# Counter 之間可以直接做加法，表示把兩份統計結果合併起來。
# 合併後的結果會把相同鍵的次數相加，適合處理分批統計再彙總的情境。
extra = Counter(["banana", "cherry"])
print("合併：", cnt + extra)

# ── defaultdict：有預設值的 dict ─────────────────────────
# defaultdict 的重點在於：當存取不存在的鍵時，它會自動建立預設值。
# 這讓「分組」與「累加」的程式碼可以少寫很多 if 判斷。

# 按類別分組
# records 每筆資料是一個二元組：(系所, 姓名)
records = [
    ("系資", "Alice"),
    ("電子", "Bob"),
    ("系資", "Carol"),
    ("電子", "David"),
    ("系資", "Eve"),
]

# defaultdict(list) 表示每個新鍵都會自動對應到一個空 list。
# 因此第一次看到某個系所時，可以直接 append，不需要先檢查鍵是否存在。
by_dept = defaultdict(list)
for dept, name in records:
    by_dept[dept].append(name)

print("\ndefaultdict：")
for dept, members in by_dept.items():
    # 每個 key 對應一組同系所的成員名單
    print(f"  {dept}: {members}")

# defaultdict(int) 的預設值是 0，很適合做計數或累加。
# 例如統計每個人的總分、每個分類的數量、每個月份的銷售額等。
score_sum = defaultdict(int)
scores = [("Alice", 90), ("Bob", 80), ("Alice", 85), ("Bob", 70)]
for name, score in scores:
    # 若 name 還沒出現過，score_sum[name] 會自動是 0
    # 所以可以直接加分，不需要先初始化
    score_sum[name] += score
print("\n各人總分：", dict(score_sum))

# ── namedtuple：具名結構，更可讀 ─────────────────────────
# namedtuple 用來建立「像 tuple 一樣輕量，但欄位有名字」的資料結構。
# 與一般 tuple 相比，它可以用屬性名稱存取欄位，讓程式碼更清楚。
# 常見用途：一筆股票資料、一筆座標、一筆查詢結果。
Stock = namedtuple("Stock", ["symbol", "price", "change"])
s = Stock("AA", 39.48, -0.18)

# 使用 .symbol、.price、.change 比用索引 [0]、[1]、[2] 更容易閱讀。
print(f"\n{s.symbol}: ${s.price}  漲跌 {s.change}")

# ── 綜合：從 list of dict 做統計 ─────────────────────────
# 這段示範如何從一組字典資料中，按照 dept 分組後再計算平均分數。
# 這種流程非常常見，例如：
#   - 依部門統計平均績效
#   - 依班級計算平均成績
#   - 依城市統計平均銷售額
data = [
    {"dept": "系資", "score": 85},
    {"dept": "電子", "score": 78},
    {"dept": "系資", "score": 92},
    {"dept": "電子", "score": 88},
]

# defaultdict(list) 先把每個系所的分數收集成一個清單。
# 之後再對每個清單計算平均值，這樣邏輯會很清楚。
dept_scores = defaultdict(list)
for row in data:
    # row["dept"] 是分組鍵，row["score"] 是要累積的值
    dept_scores[row["dept"]].append(row["score"])

print("\n各系平均：")
for dept, scores in dept_scores.items():
    # sum(scores) 計算總分，len(scores) 計算人數
    # 平均值 = 總分 / 數量
    avg = sum(scores) / len(scores)
    print(f"  {dept}: {avg:.1f}")
