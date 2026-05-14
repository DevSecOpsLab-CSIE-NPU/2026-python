# R05. 資料統計與累加（6.13）
# 主題：`Counter` / `defaultdict` / `namedtuple` 的整合應用
# 註解語言：繁體中文（臺灣 zh-TW），並補充使用場景與資料結構特性

from collections import Counter, defaultdict, namedtuple

# ── Counter：計數器 ──────────────────────────────────────
# `Counter` 是 `dict` 的特化版本，專門用來「計算元素出現次數」。
# 與其他字典不同的是，它內建了許多統計相關的方法，例如 `most_common()`。
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# 直接把列表丟給 Counter，它會自動計算每個元素出現的次數。
cnt = Counter(words)
print("Counter：", cnt)

# `most_common()` 方法會回傳出現次數最多的 N 個元素與它們的計數。
# 結果是一個 list of tuples，內容按計數從高到低排序。
print("最多出現：", cnt.most_common(2))      # [('apple', 3), ('banana', 2)]

# Counter 物件可以直接相加，用來合併多個計數結果。
# 這在合併來自不同來源的統計資料時特別有用。
extra = Counter(["banana", "cherry"])
print("合併：", cnt + extra)

# ── defaultdict：有預設值的 dict ─────────────────────────
# 一般 `dict` 在存取不存在的 key 時會丟出 `KeyError`。
# `defaultdict` 則會依照指定的「工廠函式」自動建立預設值，
# 例如 `defaultdict(list)` 會在存取新 key 時自動創建一個空列表。

# 按類別分組
# 這段程式示範如何用 `defaultdict(list)` 把相同部門的人名分組。
# 若沒有 defaultdict，傳統做法需要先檢查 key 是否存在，再決定建立或追加。
records = [
    ("系資", "Alice"),
    ("電子", "Bob"),
    ("系資", "Carol"),
    ("電子", "David"),
    ("系資", "Eve"),
]

by_dept = defaultdict(list)
for dept, name in records:
    # 當第一次存取某個部門時，defaultdict 會自動建立一個空列表。
    # 後續就可以直接 `.append()` 而不用先檢查存在性。
    by_dept[dept].append(name)

print("\ndefaultdict：")
for dept, members in by_dept.items():
    print(f"  {dept}: {members}")

# defaultdict(int) 做計數
# `defaultdict(int)` 常用於計數或累加場景，因為 `int()` 的預設值是 `0`。
# 這比傳統的「先檢查 key 再累加」更簡潔。
score_sum = defaultdict(int)
scores = [("Alice", 90), ("Bob", 80), ("Alice", 85), ("Bob", 70)]
for name, score in scores:
    # 若 `name` 是第一次出現，`score_sum[name]` 會自動初始化為 0，
    # 然後加上目前分數。
    score_sum[name] += score
print("\n各人總分：", dict(score_sum))

# ── namedtuple：具名結構，更可讀 ─────────────────────────
# `namedtuple` 讓你建立輕量級的「具名欄位」物件，比普通 tuple 更易讀。
# 相比 `dict`，它的記憶體用量更少；相比普通 tuple，存取時可用屬性名而不必記位置。
#
# `namedtuple("Stock", ["symbol", "price", "change"])` 會建立一個新的類別，
# 其實體可以這樣建立：`Stock("AA", 39.48, -0.18)`。
Stock = namedtuple("Stock", ["symbol", "price", "change"])

# 透過屬性名存取欄位，程式碼更容易理解。
s = Stock("AA", 39.48, -0.18)
print(f"\n{s.symbol}: ${s.price}  漲跌 {s.change}")

# ── 綜合：從 list of dict 做統計 ─────────────────────────
# 這段範例綜合展示：從一群 dict（例如從 CSV 或 API 讀進來的資料）
# 如何用 defaultdict 分組，然後計算統計量（例如平均值）。
data = [
    {"dept": "系資", "score": 85},
    {"dept": "電子", "score": 78},
    {"dept": "系資", "score": 92},
    {"dept": "電子", "score": 88},
]

# 用 defaultdict 把同系別的分數集中在一起
dept_scores = defaultdict(list)
for row in data:
    dept_scores[row["dept"]].append(row["score"])

# 逐系計算平均分數
print("\n各系平均：")
for dept, scores in dept_scores.items():
    avg = sum(scores) / len(scores)
    print(f"  {dept}: {avg:.1f}")

# ── 常見提醒 ─────────────────────────────────────────────
# - `Counter` 適合「計數」；若只是想分組，`defaultdict(list)` 通常更簡潔。
# - `defaultdict` 的工廠函式可以自訂，例如 `defaultdict(lambda: 0)` 也可以做計數。
# - `namedtuple` 是不可變的 (immutable)，建立後不能改欄位值；若需要可變性，考慮用一般 `class`。
# - 三者都能搭配 `sorted()`、list comprehension 做進一步處理。
