# 9 比較、排序與 key 函式範例

# 比較運算（tuple 逐一比較）
# 先比較第 1 個元素；若相同再比較第 2 個元素
a = (1, 2)
b = (1, 3)
# 因為前者第 2 個元素 2 < 3，所以結果為 True
result = a < b

# key 排序
# 每筆資料是字典，這裡要依 uid 欄位由小到大排序
rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]
# key 函式告訴 sorted: 用每列的 r['uid'] 當排序依據
rows_sorted = sorted(rows, key=lambda r: r['uid'])

# min/max 搭配 key
# 在 rows 中找出 uid 最小的那一筆字典
smallest = min(rows, key=lambda r: r['uid'])

# ========================================
# 輸出範例：看看每個變數的實際結果
# ========================================
print("=== tuple 比較 ===")
print(f"a = {a}")
print(f"b = {b}")
print(f"a < b 的結果是: {result}")
print()

print("=== 排序（sorted with key） ===")
print(f"原始 rows: {rows}")
print(f"按 uid 排序後: {rows_sorted}")
print()

print("=== 找最小值（min with key） ===")
print(f"uid 最小的那筆: {smallest}")
