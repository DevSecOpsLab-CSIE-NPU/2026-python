# U8. 字典最值為何常用 zip(values, keys)（1.8）

prices = {'A': 2.0, 'B': 1.0}

min(prices)            # 回傳字典 key 的最小値（字母序），跟 value 大小無關
min(prices.values())   # 回傳最小 value，但不知道對應哪個 key

min(zip(prices.values(), prices.keys()))
# zip 將 (value, key) 配對成 tuple
# tuple 比較先比第一個元素（value）
# 因此 min/max 能同時拿到最小 value 和對應的 key，結果為 (1.0, 'B')
