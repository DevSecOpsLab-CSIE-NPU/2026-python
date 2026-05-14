# R05. 資料統計與累加（6.13）
# Counter / defaultdict / namedtuple 整合應用

from collections import Counter, defaultdict, namedtuple

# 這份示範重點：
# 1) Counter：漂亮的計數器，取代 dict 的手動計數
# 2) defaultdict：有預設值的 dict，可以避免 KeyError
# 3) namedtuple：適切之時，比一般 tuple 更易讀，組構更清晰

# ── Counter：計數器 ──────────────────────────────────────
# Counter 是 dict 的子類，自動統計序列中每個元素的出現次數
# 想計算每個元素的數量時，用 Counter 會比手動記錄方便
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
cnt = Counter(words)
# Counter 的輸出是一個 dict，key 是元素名稱，value 是計數
print("Counter：", cnt)
# most_common(n) 會回傳出現次數最多的 n 個元素，以 list of tuple 形式
print("最多出現：", cnt.most_common(2))      # [('apple', 3), ('banana', 2)]

# Counter 的加法：第二個 Counter 的 count 會加到第一個 Counter 中
extra = Counter(["banana", "cherry"])
# apple 3+0=3, banana 2+1=3, cherry 1+1=2
print("合併：", cnt + extra)

# ── defaultdict：有預設值的 dict ─────────────────────────
# defaultdict 會自動為沒有的 key 初始化預設值。常見用途：
# - defaultdict(list)   ：適合分組、整理
# - defaultdict(int)    ：適合計數、累加
# - defaultdict(set)    ：適合去除重複
# 按類別分組
records = [
    ("系資", "Alice"),
    ("電子", "Bob"),
    ("系資", "Carol"),
    ("電子", "David"),
    ("系資", "Eve"),
]

# 用 defaultdict(list) 按系別分組
# 常見的方式：如果 key 不存在，defaultdict 會自動初始化一個 []
by_dept = defaultdict(list)
for dept, name in records:
    by_dept[dept].append(name)  # 第一次 append 時，假的 key 會自動創建一個 []

print("\ndefaultdict：")
for dept, members in by_dept.items():
    print(f"  {dept}: {members}")

# defaultdict(int) 做計數 / 累加
# 整數的預設值是 0，所以可以直接 += 而不用 if key in dict
score_sum = defaultdict(int)
scores = [("Alice", 90), ("Bob", 80), ("Alice", 85), ("Bob", 70)]
for name, score in scores:
    # 第一次訪取 score_sum["Alice"] 時，計數會初始化為 0，然後加上 90
    score_sum[name] += score
print("\n各人總分：", dict(score_sum))

# ── namedtuple：具名結構，更可讀 ─────────────────────────
# namedtuple 是 tuple 的簡化版本，加上了欄位名稱
# 可讀性更好，加上了欄位名稱，自動打包 __repr__
Stock = namedtuple("Stock", ["symbol", "price", "change"])
# 這隻 tuple，也可以用位置引數 s[0]，但用欄位字段名 s.symbol 更易讀
s = Stock("AA", 39.48, -0.18)
print(f"\n{s.symbol}: ${s.price}  漲跌 {s.change}")  # AA: $39.48  漲跌 -0.18

# ── 綜合：從 list of dict 做統計 ─────────────────────────
# 實務場景：後端從數據庫或 API 取回 list of dict。
# 下面示範如何走訪計算各系的平均分數。
data = [
    {"dept": "系資", "score": 85},
    {"dept": "電子", "score": 78},
    {"dept": "系資", "score": 92},
    {"dept": "電子", "score": 88},
]

# 第一步：序釋數據推斗，按系分組
dept_scores = defaultdict(list)
for row in data:
    dept_scores[row["dept"]].append(row["score"])
    # 結匯：{'系資': [85, 92], '電子': [78, 88]}

print("\n各系平均：")
for dept, scores in dept_scores.items():
    # 第二步：為各系計算平均
    avg = sum(scores) / len(scores)
    # {:.1f} 是格式描述，表示保留 1 位小數
    print(f"  {dept}: {avg:.1f}")  # 系資: 88.5, 電子: 83.0
