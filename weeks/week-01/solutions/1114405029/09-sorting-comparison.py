# 9 比較、排序與 key 函式 (Task 實戰風格版)

# === 1. Tuple 的比較機制 (Lexicographical Order) ===
# 核心邏輯：從左到右逐一比對。一旦前面的元素分出勝負，後面就不再檢查。
# 應用：為什麼 (priority, index, item) 可以穩定排序？
a = (1, 10, "apple")
b = (1, 5, "banana")
c = (2, 1, "cherry")

# a vs b: 第一位 1 == 1，第二位 10 > 5，勝負已分！a > b 為 True (不論字串長短)
# b vs c: 第一位 1 < 2，勝負已分！c > b 為 True

print(a > b)  # Output: True
print(c > a)  # Output: True

# === 2. sorted() 與 key 函式 (以學生排序為例) ===
# key 函式的作用：告訴 Python「拿什麼」來代表這個物件進行比較。
students = [("ian", 88, 19), ("bob", 88, 19), ("amy", 95, 20)]

# 需求：分數降序 (-score) -> 年齡升序 (age) -> 姓名升序 (name)
# 語法：sorted(可迭代物件, key=lambda x: (條件1, 條件2, ...))
ranked = sorted(students, key=lambda x: (-x[1], x[2], x[0]))

print(ranked)
# Output: [('amy', 95, 20), ('bob', 88, 19), ('ian', 88, 19)]
# 技巧：數值加負號 (-) 是「反轉單一條件方向」最有效的方法。

# === 3. 字典/物件的 Top-N 排序 (以 Task 3 為例) ===
# 應用情境：從統計字典中找出出現頻率最高的前兩名
counts = {'login': 5, 'logout': 3, 'click': 5}

# 規則：次數降序 (-v), 動作升序 (k)
# 處理：使用 .items() 轉換為 list of tuples 後排序
top_n = sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:2]

print(top_n)  # Output: [('click', 5), ('login', 5)]

# === 4. 進階工具：itemgetter ===
# 用途：當你需要對特定索引排序，且資料量極大（萬筆以上）時，效能比 lambda 更優。
from operator import itemgetter

data = [('A', 10), ('B', 5), ('C', 10)]
# 僅按第二個欄位 (索引 1) 升序排序
data.sort(key=itemgetter(1))

print(data)  # Output: [('B', 5), ('A', 10), ('C', 10)]