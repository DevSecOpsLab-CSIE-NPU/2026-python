# 9 比較、排序與 key 函式範例
# Demonstrates tuple comparison, sorting with key, and min/max with key.

# 比較運算（tuple 逐一比較）
a = (1, 2)  # 建立兩個元組
b = (1, 3)
result = a < b  # Python 會逐元素比較：先比較第一個元素 1 vs 1，再比較第二個 2 vs 3，結果為 True

# key 排序
rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]  # 一個列表，內含多個字典
rows_sorted = sorted(rows, key=lambda r: r['uid'])  # 使用 uid 欄位作為排序鍵，產生新列表

# min/max 搭配 key
smallest = min(rows, key=lambda r: r['uid'])  # 找到 uid 值最小的字典


print("smallest =", smallest)  # 輸出結果