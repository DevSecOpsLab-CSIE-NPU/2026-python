# U8. 字典最值為何常用 zip(values, keys)（1.8）

prices = {'A': 2.0, 'B': 1.0}

min(prices)            # 回傳 key 的最小值（字母序）
min(prices.values())   # 回傳最小 value，但你不知道是哪個 key

min(zip(prices.values(), prices.keys()))
# 回傳 (最小value, 對應key)，一次拿到兩者
