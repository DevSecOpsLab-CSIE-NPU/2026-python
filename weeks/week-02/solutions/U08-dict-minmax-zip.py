# U8. 字典最值為何常用 zip(values, keys)（1.8）
#
# dict 的 min/max 預設比較的是 key，而非 value。
# 因此如果要找出最小/最大 value 並同時取得對應的 key，
# 可以把 values 和 keys zip 起來，讓 min/max 直接比較 value。
#
# 注意：zip 會按照對應位置配對，所以要先取 values 再取 keys，
# 才能保證取得正確的 (value, key) 對。

prices = {'A': 2.0, 'B': 1.0}

min(prices)            # 回傳 key 的最小值（以字母序比較，結果為 'A'）
min(prices.values())   # 回傳最小 value，但你不知道是哪個 key

min(zip(prices.values(), prices.keys()))
# 回傳 (最小 value, 對應的 key)，一次拿到兩者
