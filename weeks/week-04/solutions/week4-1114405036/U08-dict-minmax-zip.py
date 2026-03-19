# U8. 字典最值：zip(values, keys)（範例 1.8）
# 原理：直接對 dict 做 min() 會比 key；對 dict.values() 做會比值但拿不到 key。
# 使用 zip 將 (value, key) 反轉過來，min() 就會先比值，並同時回傳對應的 key。

prices = {'A': 2.0, 'B': 1.0}

# 一次拿到最小價格及其股票名稱
min_price = min(zip(prices.values(), prices.keys())) # (1.0, 'B')