"""U08: 為什麼常見寫法是 zip(values, keys)。"""

prices = {'A': 2.0, 'B': 1.0, 'C': 3.5}

# min(prices) 是比 key 字母，不是比價格
print('min(prices) ->', min(prices))
print('min(prices.values()) ->', min(prices.values()))

# 用 zip 把 value 跟 key 綁在一起，能同時得到「最小價格與其 key」
min_pair = min(zip(prices.values(), prices.keys()))
max_pair = max(zip(prices.values(), prices.keys()))
print('最小 (value, key):', min_pair)
print('最大 (value, key):', max_pair)
