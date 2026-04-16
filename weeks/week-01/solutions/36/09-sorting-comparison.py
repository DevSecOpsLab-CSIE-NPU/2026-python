# 09-sorting-comparison.py
# 範例：比較、排序與 key 函式

from operator import itemgetter

# 直接比較數字
print(f"3 < 5: {3 < 5}")

# 排序範例：根據物件屬性排序
data = [
    {'name': 'Alice', 'price': 30},
    {'name': 'Bob', 'price': 20},
    {'name': 'Carol', 'price': 40},
]

# 使用 lambda 作為 key 函式，根據 price 排序
sorted_by_price = sorted(data, key=lambda x: x['price'])
print(f"依 price 排序: {sorted_by_price}")

# 使用 itemgetter 作為 key 函式，效果相同
sorted_by_price_2 = sorted(data, key=itemgetter('price'))
print(f"itemgetter 排序: {sorted_by_price_2}")

# tuple 比較順序範例：先比較第一個元素，再比較第二個元素
pairs = [(1, 5), (1, 2), (0, 9)]
print(f"tuple 排序前: {pairs}")
print(f"tuple 排序後: {sorted(pairs)}")

# 為何 (priority, index, item) 可排序：
# 先比較 priority，再比較 index，最後比較 item
items = [
    (1, 2, 'taskA'),
    (1, 1, 'taskB'),
    (2, 0, 'taskC'),
]
print(f"優先排序結果: {sorted(items)}")

# Top-N 範例：取前三大元素
scores = [50, 90, 70, 80]
print(f"前三大成績: {sorted(scores, reverse=True)[:3]}")
