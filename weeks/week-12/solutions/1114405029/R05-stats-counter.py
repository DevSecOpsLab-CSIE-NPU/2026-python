# R05. 資料統計與累加（6.13）
# Counter / defaultdict / namedtuple 整合應用

# 從 collections 模組匯入：
# Counter      → 計數器
# defaultdict  → 有預設值的 dictionary
# namedtuple   → 具名稱欄位的 tuple

# collections 是 Python 內建模組
# 提供許多進階資料結構
from collections import Counter, defaultdict, namedtuple

# ── Counter：計數器 ──────────────────────────────────────

# 建立一個字串 list
# 裡面有重複單字
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# Counter(words)：
# 自動統計每個元素出現次數

# 回傳型態是 Counter
# 本質上類似 dictionary

# 結果：
# apple  → 3 次
# banana → 2 次
# cherry → 1 次
cnt = Counter(words)

# 印出 Counter 結果
print("Counter：", cnt)

# cnt.most_common(2)：
# 取得出現次數最多的前 2 名

# 回傳 list
# 每個元素是 tuple：
# (元素名稱, 出現次數)

# 結果：
# [('apple', 3), ('banana', 2)]
print("最多出現：", cnt.most_common(2))      # [('apple', 3), ('banana', 2)]

# 可直接相加合併

# 建立另一個 Counter
extra = Counter(["banana", "cherry"])

# Counter 可以直接使用 +
# 相同 key 的數量會相加

# 原本：
# banana → 2
# cherry → 1

# extra：
# banana → 1
# cherry → 1

# 合併後：
# banana → 3
# cherry → 2
print("合併：", cnt + extra)

# ── defaultdict：有預設值的 dict ─────────────────────────

# 按類別分組

# records：
# 每個 tuple 包含：
# (科系, 名字)
records = [
    ("系資", "Alice"),
    ("電子", "Bob"),
    ("系資", "Carol"),
    ("電子", "David"),
    ("系資", "Eve"),
]

# defaultdict(list)：
# 當 key 不存在時
# 自動建立空 list []

# 不需要先判斷：
# if key not in dict
by_dept = defaultdict(list)

# 逐筆處理 records
for dept, name in records:

    # 將 name 加入對應科系 list
    # 如果 dept 不存在：
    # defaultdict 會自動建立空 list
    by_dept[dept].append(name)

# 印出 defaultdict 結果
print("\ndefaultdict：")

# by_dept.items()：
# 同時取得 key 與 value
for dept, members in by_dept.items():

    # dept    → 科系名稱
    # members → 該科系所有學生 list
    print(f"  {dept}: {members}")

# defaultdict(int) 做計數

# defaultdict(int)：
# key 不存在時
# 自動給預設值 0

# 很適合：
# 1. 累加
# 2. 統計
# 3. 計數
score_sum = defaultdict(int)

# scores：
# 每個 tuple：
# (名字, 分數)
scores = [("Alice", 90), ("Bob", 80), ("Alice", 85), ("Bob", 70)]

# 逐筆累加分數
for name, score in scores:

    # 第一次出現時：
    # defaultdict(int) 會自動給 0

    # 例如：
    # score_sum["Alice"] += 90
    # 等同：
    # 0 + 90
    score_sum[name] += score

# defaultdict 印出時格式較特殊
# 轉成 dict 比較容易閱讀
print("\n各人總分：", dict(score_sum))

# ── namedtuple：具名結構，更可讀 ─────────────────────────

# namedtuple()：
# 建立「具名稱欄位」的 tuple 類型

# 第一個參數：
# 類型名稱 → "Stock"

# 第二個參數：
# 欄位名稱 list
# ["symbol", "price", "change"]

# 建立後：
# 可以用 .symbol 存取
# 可讀性比一般 tuple 高很多
Stock = namedtuple("Stock", ["symbol", "price", "change"])

# 建立 Stock 物件
s = Stock("AA", 39.48, -0.18)

# 使用欄位名稱存取資料
# s.symbol → 股票代號
# s.price  → 價格
# s.change → 漲跌
print(f"\n{s.symbol}: ${s.price}  漲跌 {s.change}")

# ── 綜合：從 list of dict 做統計 ─────────────────────────

# data：
# list 裡面每個元素都是 dictionary

# 每筆資料包含：
# dept  → 科系
# score → 分數
data = [
    {"dept": "系資", "score": 85},
    {"dept": "電子", "score": 78},
    {"dept": "系資", "score": 92},
    {"dept": "電子", "score": 88},
]

# defaultdict(list)：
# 用來儲存每個科系所有分數
dept_scores = defaultdict(list)

# 逐筆處理 data
for row in data:

    # row["dept"]：
    # 取得科系

    # row["score"]：
    # 取得分數

    # 將分數加入對應科系 list
    dept_scores[row["dept"]].append(row["score"])

# 印出平均分數
print("\n各系平均：")

# 遍歷每個科系與分數 list
for dept, scores in dept_scores.items():

    # sum(scores)：
    # 計算總分

    # len(scores)：
    # 計算人數

    # 平均 = 總分 / 人數
    avg = sum(scores) / len(scores)

    # :.1f：
    # 浮點數保留 1 位小數
    print(f"  {dept}: {avg:.1f}")