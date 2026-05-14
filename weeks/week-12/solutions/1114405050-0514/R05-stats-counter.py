# R05. 資料統計與累加（6.13）
# Counter / defaultdict / namedtuple 整合應用

from collections import Counter, defaultdict, namedtuple

# ── Counter：計數器 ──────────────────────────────────────
# Counter 是一個特殊的字典，專門用來計算元素出現的次數
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
cnt = Counter(words)
print("Counter：", cnt)
# most_common(n) 可以直接取出出現次數最多的前 n 個元素，回傳格式為 list of tuples
print("最多出現：", cnt.most_common(2))      # [('apple', 3), ('banana', 2)]

# 可直接相加合併
# Counter 支援數學運算符號，可以直接用加號將兩個 Counter 統計結果合併
extra = Counter(["banana", "cherry"])
print("合併：", cnt + extra)

# ── defaultdict：有預設值的 dict ─────────────────────────
# 按類別分組
# 一般 dict 若 key 不存在會報 KeyError，defaultdict 在 key 不存在時會自動呼叫傳入的型別/函式來建立預設值
records = [
    ("系資", "Alice"),
    ("電子", "Bob"),
    ("系資", "Carol"),
    ("電子", "David"),
    ("系資", "Eve"),
]

# defaultdict(list) 代表若 key 不存在，預設值會是一個空清單 []
by_dept = defaultdict(list)
for dept, name in records:
    # 不需要寫 if dept not in by_dept: by_dept[dept] = [] 這樣的檢查，程式碼更簡潔
    by_dept[dept].append(name)

print("\ndefaultdict：")
for dept, members in by_dept.items():
    print(f"  {dept}: {members}")

# defaultdict(int) 做計數
# defaultdict(int) 代表若 key 不存在，預設值為 0（因為 int() 回傳 0）
score_sum = defaultdict(int)
scores = [("Alice", 90), ("Bob", 80), ("Alice", 85), ("Bob", 70)]
for name, score in scores:
    # 可以直接累加，不需要檢查 key 是否已經存在
    score_sum[name] += score
print("\n各人總分：", dict(score_sum))

# ── namedtuple：具名結構，更可讀 ─────────────────────────
# namedtuple 讓我們可以建立一個類似 tuple 的物件，但可以用「名稱」來存取屬性，而不只是用索引數字
Stock = namedtuple("Stock", ["symbol", "price", "change"])
s = Stock("AA", 39.48, -0.18)
# 用 s.symbol 取代 s[0]，大幅提升程式的可讀性
print(f"\n{s.symbol}: ${s.price}  漲跌 {s.change}")

# ── 綜合：從 list of dict 做統計 ─────────────────────────
# 實務上常見的情境：處理一連串帶有相同結構的字典資料
data = [
    {"dept": "系資", "score": 85},
    {"dept": "電子", "score": 78},
    {"dept": "系資", "score": 92},
    {"dept": "電子", "score": 88},
]

# 使用 defaultdict 快速依據科系 (dept) 將分數 (score) 分組收集
dept_scores = defaultdict(list)
for row in data:
    dept_scores[row["dept"]].append(row["score"])

print("\n各系平均：")
# 計算分組收集後的平均值
for dept, scores in dept_scores.items():
    avg = sum(scores) / len(scores)
    print(f"  {dept}: {avg:.1f}")
