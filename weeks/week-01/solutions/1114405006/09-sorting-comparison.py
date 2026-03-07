# 9 比較、排序與 key 函式範例

# 比較運算（tuple 逐一比較）
a = (1, 2)
b = (1, 3)
result = a < b

# key 排序
rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]
rows_sorted = sorted(rows, key=lambda r: r['uid'])

# min/max 搭配 key
smallest = min(rows, key=lambda r: r['uid'])
