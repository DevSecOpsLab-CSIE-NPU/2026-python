# U8. 字典最值為何常用 zip(values, keys)（1.8）
#
# dict 的 min/max 預設比較的是 key，而非 value。
# 因此如果要找出最小/最大 value 並同時取得對應的 key，
# 可以把 values 和 keys zip 起來，讓 min/max 直接比較 value。
#
# 注意：zip 會按照對應位置配對，所以要先取 values 再取 keys，
# 才能保證取得正確的 (value, key) 對。

prices = {'A': 2.0, 'B': 1.0, 'C': 1.0}

# 1. 你的 zip 解法（最直觀且高效）
# 注意：若 value 相同，則會比較 key 的字母序
min_price_tuple = min(zip(prices.values(), prices.keys()))
print(f"1. zip 組合極小值: {min_price_tuple}") 
# 輸出: (1.0, 'B')

# 2. 另一種常見寫法：使用 min 的 key 參數
# 優點：直接回傳原始字典的 key，不需額外建立 zip 物件
min_key = min(prices, key=lambda k: prices[k])
print(f"2. 價格最低的 Key: '{min_key}' (價格為 {prices[min_key]})")

# 3. 排序範例 (配合 zip)
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(f"3. 依價格排序後的清單: {prices_sorted}")
# 回傳 (最小 value, 對應的 key)，一次拿到兩者
