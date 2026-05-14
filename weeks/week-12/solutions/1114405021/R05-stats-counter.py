# R05. 資料統計與累加（6.13）
# 本範例示範 collections 模組中三個非常實用的工具：
# 1. Counter：用來計數與找出出現次數最多的項目
# 2. defaultdict：有預設值的字典，適合分組與累加
# 3. namedtuple：建立具名欄位的輕量級資料結構

from collections import Counter, defaultdict, namedtuple

# -----------------------------------------------------------------------------
# 一、Counter：計數器
# -----------------------------------------------------------------------------
# Counter 的用途是統計每個元素出現的次數。
# 它特別適合處理單字統計、標籤統計、商品銷量排行等情境。
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# Counter 會自動把清單中的每個元素計數。
# 結果會是一個類似字典的物件：元素作為 key，次數作為 value。
cnt = Counter(words)
print("Counter：", cnt)

# most_common(n) 會回傳出現次數最多的前 n 個項目，格式是 [(元素, 次數), ...]
# 這裡取前 2 名，可以快速找出熱門項目。
print("最多出現：", cnt.most_common(2))      # [('apple', 3), ('banana', 2)]

# Counter 之間可以直接相加。
# 這會把兩個計數器中相同 key 的次數加總，非常適合合併多份統計結果。
extra = Counter(["banana", "cherry"])
print("合併：", cnt + extra)

# -----------------------------------------------------------------------------
# 二、defaultdict：有預設值的 dict
# -----------------------------------------------------------------------------
# 一般 dict 如果 key 不存在，直接存取會發生 KeyError。
# defaultdict 則會在 key 不存在時自動建立預設值，
# 因此非常適合「累加」或「分組」這類需要不斷新增 key 的情境。

# 這裡示範依照科系分組學生姓名。
records = [
    ("系資", "Alice"),
    ("電子", "Bob"),
    ("系資", "Carol"),
    ("電子", "David"),
    ("系資", "Eve"),
]

# defaultdict(list) 代表每次遇到新 key 時，自動給一個空串列 []。
# 這樣我們就可以直接 append，不需要先檢查 key 是否存在。
by_dept = defaultdict(list)
for dept, name in records:
    by_dept[dept].append(name)

print("\ndefaultdict：")
for dept, members in by_dept.items():
    print(f"  {dept}: {members}")

# defaultdict(int) 代表每次遇到新 key 時，自動給 0。
# 這非常適合做加總、計數、分數累積等動作。
score_sum = defaultdict(int)
scores = [("Alice", 90), ("Bob", 80), ("Alice", 85), ("Bob", 70)]
for name, score in scores:
    score_sum[name] += score
print("\n各人總分：", dict(score_sum))

# -----------------------------------------------------------------------------
# 三、namedtuple：具名結構，更可讀
# -----------------------------------------------------------------------------
# namedtuple 可以建立一種像 tuple、但欄位有名稱的資料結構。
# 這樣做的好處是：
# - 仍然輕量
# - 可以用屬性名稱讀取資料
# - 程式比純索引 tuple 更容易理解
Stock = namedtuple("Stock", ["symbol", "price", "change"])

# 建立一筆股票資料。
# 如果使用一般 tuple，你必須記住第 1、2、3 個欄位分別是什麼；
# 使用 namedtuple 後，可以直接用 .symbol、.price、.change 讀取。
s = Stock("AA", 39.48, -0.18)
print(f"\n{s.symbol}: ${s.price}  漲跌 {s.change}")

# -----------------------------------------------------------------------------
# 四、綜合應用：從 list of dict 做統計
# -----------------------------------------------------------------------------
# 真實資料常常是「一筆資料一個 dict」，例如從 JSON、CSV 轉進來的內容。
# 下面示範如何先按科系分組，再計算各科系平均分數。
data = [
    {"dept": "系資", "score": 85},
    {"dept": "電子", "score": 78},
    {"dept": "系資", "score": 92},
    {"dept": "電子", "score": 88},
]

# defaultdict(list) 可以讓我們快速把同一科系的分數收集到同一個 list 裡。
dept_scores = defaultdict(list)
for row in data:
    dept_scores[row["dept"]].append(row["score"])

print("\n各系平均：")
for dept, scores in dept_scores.items():
    # 平均值 = 總和 / 筆數
    avg = sum(scores) / len(scores)
    print(f"  {dept}: {avg:.1f}")

# -----------------------------------------------------------------------------
# 補充說明
# -----------------------------------------------------------------------------
# Counter：偏向「次數統計」
# defaultdict：偏向「分組與累加」
# namedtuple：偏向「結構化資料表達」
#
# 三者常常一起使用，尤其在處理文字分析、資料清理、統計報表時非常方便。
