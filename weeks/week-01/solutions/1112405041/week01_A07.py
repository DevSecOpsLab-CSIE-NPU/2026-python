# 【Bloom 階段：U - 理解與進階應用】
# 7 函式與 lambda 範例
# August 的惡意提醒：不要寫太長的 lambda。
# 如果邏輯超過一行，請乖乖定義一般的 def，否則助教會在 Code Style (20分) 扣你分。

def double(x):
    """定義具名函式，提高代碼複用性與可讀性"""
    return x * 2

values = [1, 2, 3]
# 搭配推導式呼叫函式
result = [double(x) for x in values]

# Lambda 做為排序的 Key
# 在 Week 02 Task 2 的學生排名中，這是「必殺技」
rows = [
    {'name': 'A', 'score': 90},
    {'name': 'B', 'score': 75}
]
# 根據分數從低到高排序
rows_sorted = sorted(rows, key=lambda r: r['score'])

print(f"Result: {result}")
print(f"Sorted Rows: {rows_sorted}")
