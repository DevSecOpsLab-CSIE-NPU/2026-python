# R05. 資料統計與累加（6.13）
# Counter / defaultdict / namedtuple 整合應用
#
# 這個範例主要示範 collections 模組中三個很常用的工具：
# 1. Counter：快速統計元素出現次數。
# 2. defaultdict：當 key 不存在時，自動提供預設值。
# 3. namedtuple：建立有欄位名稱的輕量資料結構。

from collections import Counter, defaultdict, namedtuple

# ── Counter：計數器 ──────────────────────────────────────
# Counter 很適合拿來統計清單中每個元素出現了幾次。
# 它會自動幫你把相同的值累加，不需要手動寫計數邏輯。
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
cnt = Counter(words)
# 印出來會看到每個字的出現次數，格式類似字典。
print("Counter：", cnt)
# most_common(n) 會回傳出現次數最高的前 n 個元素，結果是由高到低排序的列表。
# 這常用在找熱門關鍵字、排行榜、最常見項目等情境。
print("最多出現：", cnt.most_common(2))      # [('apple', 3), ('banana', 2)]

# 可直接相加合併
# Counter 之間可以直接做加法，會把相同 key 的次數加總。
# 這種寫法很適合把不同批次的統計結果合併在一起。
extra = Counter(["banana", "cherry"])
print("合併：", cnt + extra)

# ── defaultdict：有預設值的 dict ─────────────────────────
# defaultdict 和 dict 類似，但當你存取一個不存在的 key 時，
# 它會自動用指定的工廠函式建立預設值，而不是直接丟 KeyError。
# 按類別分組
# 這裡準備一組資料，每個 tuple 代表「系所, 姓名」。
records = [
    ("系資", "Alice"),
    ("電子", "Bob"),
    ("系資", "Carol"),
    ("電子", "David"),
    ("系資", "Eve"),
]

# defaultdict(list) 表示當某個 key 第一次出現時，預設值是一個新的空 list。
# 這樣就可以直接 append，不需要先檢查 key 存不存在。
by_dept = defaultdict(list)
for dept, name in records:
    # 這裡的寫法很簡潔：如果 by_dept[dept] 不存在，defaultdict 會先建立 []。
    # 然後再把 name 加進去，達到「依系所分組」的效果。
    by_dept[dept].append(name)

print("\ndefaultdict：")
# items() 會同時取得每個 key 與對應的值，方便逐組輸出。
for dept, members in by_dept.items():
    print(f"  {dept}: {members}")

# defaultdict(int) 做計數
# int() 的預設值是 0，所以 defaultdict(int) 很適合做累加與計數。
score_sum = defaultdict(int)
# 每筆資料是一個「姓名, 分數」的組合。
scores = [("Alice", 90), ("Bob", 80), ("Alice", 85), ("Bob", 70)]
for name, score in scores:
    # 如果 name 還沒出現過，score_sum[name] 會自動從 0 開始。
    # 然後把每次分數累加進去，就能得到每個人的總分。
    score_sum[name] += score
# dict(score_sum) 只是把 defaultdict 轉成一般 dict，輸出時更清楚。
print("\n各人總分：", dict(score_sum))

# ── namedtuple：具名結構，更可讀 ─────────────────────────
# namedtuple 用來建立一種「像 tuple，但可以用欄位名稱存取」的資料結構。
# 它很適合用來表示固定欄位的小型資料，例如股票、座標、點位等。
Stock = namedtuple("Stock", ["symbol", "price", "change"])
# 建立一筆 Stock 資料後，就能用 .symbol、.price、.change 直接取值。
s = Stock("AA", 39.48, -0.18)
print(f"\n{s.symbol}: ${s.price}  漲跌 {s.change}")

# ── 綜合：從 list of dict 做統計 ─────────────────────────
# 這段示範當資料來源是一串 dict 時，如何用 defaultdict 做分組與後續統計。
data = [
    {"dept": "系資", "score": 85},
    {"dept": "電子", "score": 78},
    {"dept": "系資", "score": 92},
    {"dept": "電子", "score": 88},
]

# 預設值是 list，表示每個系所底下會累積一串分數。
dept_scores = defaultdict(list)
for row in data:
    # 先用 row["dept"] 找到所屬系所，再把該筆分數 append 進去。
    dept_scores[row["dept"]].append(row["score"])

print("\n各系平均：")
# 逐個系所計算平均分數：sum(scores) / len(scores)
# 這裡先把每個系所的分數清單收集起來，再做統計，邏輯清楚也容易擴充。
for dept, scores in dept_scores.items():
    avg = sum(scores) / len(scores)
    print(f"  {dept}: {avg:.1f}")
