# 9 比較、排序與 key 函式範例

# 比較運算（tuple 會由左到右逐一比較）
a = (1, 2)
b = (1, 3)
# 因為前一個元素都相同，接著比較 2 < 3，所以結果為 True
result = a < b

# key 排序：依據每筆資料的 uid 由小到大排序
rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]
rows_sorted = sorted(rows, key=lambda r: r['uid'])

# min/max 搭配 key：找出 uid 最小的一筆資料
smallest = min(rows, key=lambda r: r['uid'])
