# R05. 資料統計與累加（6.13）
# Counter / defaultdict / namedtuple 整合應用

from collections import Counter, defaultdict, namedtuple

# ── Counter：計數器 ──────────────────────────────────────
# 【詳解】
# Counter 自動統計可迭代物件中每個元素的出現次數。
# 內部是 dict，鍵為元素，值為出現次數。
# most_common(n) 找出現次數最多的前 n 個（如熱門詞、排行榜）。
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
cnt = Counter(words)
print("Counter：", cnt)
print("最多出現：", cnt.most_common(2))      # [('apple', 3), ('banana', 2)]

# 可直接相加合併
extra = Counter(["banana", "cherry"])
print("合併：", cnt + extra)

# ── defaultdict：有預設值的 dict ─────────────────────────
# 【詳解】
# 普通 dict 存取不存在的鍵會 raise KeyError。
# defaultdict 提供工廠函式，不存在的鍵自動生成預設值。
# 工廠可以是 list、int、set 等容器，或任意 callable。
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
# 【詳解】
# namedtuple 是輕量版的 class，用屬性名稱而非索引存取。
# 不可變（immutable）、內存效率高、適合純資料結構。
# 如 SQL 查詢結果可轉成 namedtuple 的 list，比 dict list 更清晰。
Stock = namedtuple("Stock", ["symbol", "price", "change"])
s = Stock("AA", 39.48, -0.18)
print(f"\n{s.symbol}: ${s.price}  漲跌 {s.change}")

# ── 綜合：從 list of dict 做統計 ─────────────────────────
# 【詳解】
# 這是資料分析常見流程：讀入資料 → 分組 → 統計。
# defaultdict 適合「分組後逐行累加」的場景。
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
