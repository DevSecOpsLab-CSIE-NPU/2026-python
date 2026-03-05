# 9 比較、排序與 key 函式範例
# 本範例展示 Python 中元組比較、使用 key 函式排序，以及 min/max 函式的進階用法


# ========== 元組比較 (Tuple Comparison) ==========
# Python 對元組進行比較時，會逐一比較每個元素
# 當第一個元素相等時，會比較第二個元素，以此類推

# 定義兩個元組
a = (1, 2)  # 第一個元組：(1, 2)
b = (1, 3)  # 第二個元組：(1, 3)

# 比較結果：
# - 第一個元素都是 1，相等，繼續比較
# - 第二個元素：2 < 3，所以 a < b 為 True
result = a < b  # result = True


# ========== 使用 key 函式進行排序 (Sorted with key parameter) ==========
# sorted() 函式默認按照自然順序排序
# 使用 key 參數可以指定自定義的排序依據

# 定義包含字典的列表，每個字典有 'uid' 鍵
rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]

# 使用 sorted() 函式，按照每個字典的 'uid' 值升序排序
# lambda r: r['uid'] 是一個匿名函式，提取每個元素的 'uid' 值作為排序依據
# 結果：[{'uid': 1}, {'uid': 2}, {'uid': 3}]
rows_sorted = sorted(rows, key=lambda r: r['uid'])


# ========== min/max 函式搭配 key 參數 ==========
# min() 和 max() 函式也支持 key 參數，用於自定義比較邏輯

# 在 rows 列表中找到 'uid' 值最小的字典
# lambda r: r['uid'] 指定以 'uid' 的值進行比較
# 結果：{'uid': 1}（uid 最小的字典）
smallest = min(rows, key=lambda r: r['uid'])
