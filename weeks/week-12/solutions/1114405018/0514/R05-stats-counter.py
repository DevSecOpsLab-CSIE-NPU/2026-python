"""R05. 資料統計與累加（6.13）

說明（繁體中文詳細註解）：
- 本檔整合示範 `collections.Counter`、`defaultdict` 與 `namedtuple` 的典型用法，
  這些工具在進行資料分析、分組與簡易統計時非常實用。

簡單速記：
- Counter -> 用於計數（類似 histogram）
- defaultdict -> 帶預設值的 dict（避免 KeyError，常用於分組或累加）
- namedtuple -> 輕量級的具名結構，增加可讀性
"""

from collections import Counter, defaultdict, namedtuple


# Counter：計數器（統計序列中各元素出現的次數）
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
cnt = Counter(words)
print("Counter：", cnt)                       # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print("最多出現：", cnt.most_common(2))      # 取得出現次數最多的前兩項

# Counter 可直接相加合併（對應 key 的值會相加）
extra = Counter(["banana", "cherry"])
print("合併：", cnt + extra)


# defaultdict：有預設值的 dict，常用於分組或累加
records = [
    ("系資", "Alice"),
    ("電子", "Bob"),
    ("系資", "Carol"),
    ("電子", "David"),
    ("系資", "Eve"),
]

by_dept = defaultdict(list)    # 每個 key 預設為空 list
for dept, name in records:
    by_dept[dept].append(name)

print("\ndefaultdict（分組示例）：")
for dept, members in by_dept.items():
    print(f"  {dept}: {members}")


# defaultdict(int) 做計數或累加（預設為 0）
score_sum = defaultdict(int)
scores = [("Alice", 90), ("Bob", 80), ("Alice", 85), ("Bob", 70)]
for name, score in scores:
    score_sum[name] += score
print("\n各人總分：", dict(score_sum))


# namedtuple：定義具名的不可變結構，類似輕量版 class
Stock = namedtuple("Stock", ["symbol", "price", "change"])
s = Stock("AA", 39.48, -0.18)
print(f"\n{s.symbol}: ${s.price}  漲跌 {s.change}")


# 綜合示例：從 list of dict 做分組統計（計算各系平均）
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
