# 09.py - 比較、使用 key 排序與 min/max
# 元組逐項比較
a = (1, 2)
b = (1, 3)
result = a < b

# 使用 key 排序
rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]
rows_sorted = sorted(rows, key=lambda r: r['uid'])

# 使用 key 找最小值
smallest = min(rows, key=lambda r: r['uid'])

print(f"a = {a}")
print(f"b = {b}")
print(f"result of a < b: {result}")
print(f"rows = {rows}")
print(f"rows_sorted = {rows_sorted}")
print(f"smallest = {smallest}")