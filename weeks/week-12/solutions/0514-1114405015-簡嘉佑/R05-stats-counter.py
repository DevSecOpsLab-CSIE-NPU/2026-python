# R05. 資料統計與累加（6.13）
# Counter / defaultdict / namedtuple 整合應用
#
# collections 模組提供三個常用的容器，各有專擅場景：
#   Counter     → 自動計數，支援合併操作
#   defaultdict → 存取不存在的鍵時自動建立預設型別
#   namedtuple  → 用名稱存取欄位的重量級 tuple

from collections import Counter, defaultdict, namedtuple

# ── Counter：計數器 ──────────────────────────────────────
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
# Counter 直接接受可迭代物件，自動統計每個元素出現次數
cnt = Counter(words)
print("Counter：", cnt)
print("最多出現：", cnt.most_common(2))      # [('apple', 3), ('banana', 2)]

# Counter 支援加法合併：相同鍵的次數相加，新鍵直接加入
extra = Counter(["banana", "cherry"])
print("合併：", cnt + extra)

# ── defaultdict：有預設值的 dict ─────────────────────────
# 按類別分組
records = [
    ("系資", "Alice"),
    ("電子", "Bob"),
    ("系資", "Carol"),
    ("電子", "David"),
    ("系資", "Eve"),
]

by_dept = defaultdict(list)
for dept, name in records:
    by_dept[dept].append(name)

print("\ndefaultdict：")
for dept, members in by_dept.items():
    print(f"  {dept}: {members}")

# defaultdict(int) 做計數
score_sum = defaultdict(int)
scores = [("Alice", 90), ("Bob", 80), ("Alice", 85), ("Bob", 70)]
for name, score in scores:
    score_sum[name] += score
print("\n各人總分：", dict(score_sum))

# ── namedtuple：具名結構，更可讀 ─────────────────────────
Stock = namedtuple("Stock", ["symbol", "price", "change"])
s = Stock("AA", 39.48, -0.18)
print(f"\n{s.symbol}: ${s.price}  漲跌 {s.change}")

# ── 綜合：從 list of dict 做統計 ─────────────────────────
data = [
    {"dept": "系資", "score": 85},
    {"dept": "電子", "score": 78},
    {"dept": "系資", "score": 92},
    {"dept": "電子", "score": 88},
]

dept_scores = defaultdict(list)
for row in data:
    dept_scores[row["dept"]].append(row["score"])

print("\n各系平均：")
for dept, scores in dept_scores.items():
    avg = sum(scores) / len(scores)
    print(f"  {dept}: {avg:.1f}")
