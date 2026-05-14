# R05. 資料統計與累加（6.13）
# 本範例示範三個很常用的資料結構與技法：
# 1. Counter：計數器，快速統計可 hash 物件（如字串）出現次數
# 2. defaultdict：帶預設值的 dict，適合分組或累加時自動初始化
# 3. namedtuple：輕量且具可讀性的結構，用於替代簡單的 class

from collections import Counter, defaultdict, namedtuple

# ── Counter：計數器 ──────────────────────────────────────
# Counter 接受任何可迭代物件（例如 list），回傳元素->次數 的對映
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
cnt = Counter(words)
print("Counter：", cnt)  # 顯示每個元素的計數
# most_common(n) 回傳出現頻率最高的 n 個元素與次數
print("最多出現：", cnt.most_common(2))      # [('apple', 3), ('banana', 2)]

# Counter 支援各種集合運算，例如相加會把計數相加（合併頻率）
extra = Counter(["banana", "cherry"])  # 額外計數來源
print("合併：", cnt + extra)  # 每個 key 的計數會相加

# Counter 也支援減法、交集等操作，視需求使用

# ── defaultdict：有預設值的 dict ─────────────────────────
# defaultdict 可以避免 KeyError，當鍵不存在時自動建立預設值
# 常見用法：list（分組）、int（累加/計數）、set（去重分組）
records = [
    ("系資", "Alice"),
    ("電子", "Bob"),
    ("系資", "Carol"),
    ("電子", "David"),
    ("系資", "Eve"),
]

by_dept = defaultdict(list)  # 每個部門預設為空 list
for dept, name in records:
    # 第一次看到新 dept 時會自動建立一個空 list，然後 append
    by_dept[dept].append(name)

print("\ndefaultdict：")
for dept, members in by_dept.items():
    print(f"  {dept}: {members}")

# 使用 defaultdict(int) 做數值累加（初值為 0）
score_sum = defaultdict(int)
scores = [("Alice", 90), ("Bob", 80), ("Alice", 85), ("Bob", 70)]
for name, score in scores:
    # 如果 name 不存在，defaultdict 會自動建立 score_sum[name]=0
    score_sum[name] += score
print("\n各人總分：", dict(score_sum))  # 轉成 dict 輸出更好看

# ── namedtuple：具名結構，更可讀（比 tuple 易於理解） ─────────
# namedtuple 會產生一個輕量的類別，具有屬性存取但仍為不可變（像 tuple）
Stock = namedtuple("Stock", ["symbol", "price", "change"])
s = Stock("AA", 39.48, -0.18)
print(f"\n{s.symbol}: ${s.price}  漲跌 {s.change}")

# ── 綜合示例：從 list of dict 做分組與統計 ─────────────────
# 假設 data 是從資料庫或 CSV/JSON 讀出的一系列 dict
data = [
    {"dept": "系資", "score": 85},
    {"dept": "電子", "score": 78},
    {"dept": "系資", "score": 92},
    {"dept": "電子", "score": 88},
]

dept_scores = defaultdict(list)  # 每個系別維護一個 list 保存所有分數
for row in data:
    # 以 dept 為鍵，將 score 附加到對應的 list
    dept_scores[row["dept"]].append(row["score"])

print("\n各系平均：")
for dept, scores in dept_scores.items():
    # 計算平均時注意除以零的情況（此處假設至少有一筆資料）
    avg = sum(scores) / len(scores)
    print(f"  {dept}: {avg:.1f}")
