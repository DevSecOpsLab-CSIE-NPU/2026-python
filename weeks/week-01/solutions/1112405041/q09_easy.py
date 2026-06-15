# 主題 09：比較、排序與 key 函式 - 簡易教學版

# 比較運算（comparison operations）
a = (1, 2)
b = (1, 3)
result = a < b                  # Tuple 會逐個元素比較：1==1，但 2<3，所以 True
print(f"{a} < {b} = {result}")

# Tuple 比較的特性：從左到右逐個比較
x = (10, 5, 3)
y = (10, 5, 4)
print(f"{x} < {y} = {x < y}")   # 前兩個相等，第三個 3<4，所以 True

# 排序（sorting）
rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]
rows_sorted = sorted(rows, key=lambda r: r['uid'])
print(f"按 uid 排序: {rows_sorted}")

# min/max 搭配 key 函式
smallest = min(rows, key=lambda r: r['uid'])
largest = max(rows, key=lambda r: r['uid'])
print(f"最小 uid: {smallest}")
print(f"最大 uid: {largest}")

# 排序多個條件（tuple 比較）
items = [(2, 'b'), (1, 'd'), (1, 'a'), (2, 'a')]
items_sorted = sorted(items)    # 先按第一個元素，再按第二個
print(f"排序前: {items}")
print(f"排序後: {items_sorted}")

# 反向排序
nums = [3, 1, 4, 1, 5]
sorted_asc = sorted(nums)
sorted_desc = sorted(nums, reverse=True)
print(f"升序: {sorted_asc}")
print(f"降序: {sorted_desc}")
