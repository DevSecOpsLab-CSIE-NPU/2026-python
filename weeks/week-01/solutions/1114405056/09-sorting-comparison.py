# 9 比較、排序與 key 函式範例

# 比較運算（tuple 逐一比較）
# 元組比較是從左到右逐個元素比較，直到找到不同的元素
a = (1, 2)
b = (1, 3)
result = a < b  # 比較結果：True，因為 a[1] < b[1] (2 < 3)
print("元組比較結果:", result)

# key 排序
# sorted() 函數使用 key 參數來決定排序依據
# lambda 函數 lambda r: r['uid'] 表示以字典中的 'uid' 值作為排序鍵
rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]
rows_sorted = sorted(rows, key=lambda r: r['uid'])
print("排序後的列表:", rows_sorted)  # 輸出：按 uid 升序排列

# min/max 搭配 key
# min() 和 max() 函數也可以使用 key 參數來找到最小/最大的元素
smallest = min(rows, key=lambda r: r['uid'])
print("最小的元素:", smallest)  # 輸出：{'uid': 1}

# 也可以找到最大的元素
largest = max(rows, key=lambda r: r['uid'])
print("最大的元素:", largest)  # 輸出：{'uid': 3}
