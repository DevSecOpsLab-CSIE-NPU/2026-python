# 1. 元組比較 (Tuple Comparison)
# Python 會由左至右逐一比較元素。當第一個元素相同時，會比較第二個元素。
a = (1, 2)
b = (1, 3)
result = a < b
print(f"元組比較結果 (a < b): {result}") 

# ---------------------------------------

# 2. 使用 key 進行排序 (Sorting with key)
rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]
# lambda 告訴 Python：請根據字典中的 'uid' 數值來決定順序
rows_sorted = sorted(rows, key=lambda r: r['uid'])
print(f"排序後的結果: {rows_sorted}")

# ---------------------------------------

# 3. min/max 搭配 key
# 同樣使用 lambda 抓取 'uid'，找出該欄位最小的整個字典物件
smallest = min(rows, key=lambda r: r['uid'])
print(f"UID 最小的資料: {smallest}")