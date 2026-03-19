# U8. 字典最值為何常用 zip(values, keys)（1.8）

prices = {'A': 2.0, 'B': 1.0}

min(prices)
# → 'A'
# 這是因為 min(dict) 只會比較 key（字母序），不是你要的 value

min(prices.values())
# → 1.0
# 雖然拿到最小 value，但不知道是哪個 key

# 正解：用 zip 把 (value, key) 綁在一起
min(zip(prices.values(), prices.keys()))
# → (1.0, 'B')
# 一次拿到最小 value 以及對應的 key