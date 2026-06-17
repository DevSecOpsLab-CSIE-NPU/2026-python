# 9 比較、排序與 key 函式範例

a = (1, 2)
b = (1, 3)
result = a < b

rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]
rows_sorted = sorted(rows, key=lambda r: r['uid'])

smallest = min(rows, key=lambda r: r['uid'])

print(f"(1,2) < (1,3): {result}")
print(f"Sorted: {rows_sorted}")
print(f"Smallest uid: {smallest}")
