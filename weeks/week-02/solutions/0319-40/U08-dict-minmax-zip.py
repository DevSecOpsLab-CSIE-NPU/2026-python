# U8. 字典最值為何常用 zip(values, keys)（1.8）

prices = {'A': 2.0, 'B': 1.0}

print('min(prices) =', min(prices))                    # key 的最小值（字母序）
print('min(prices.values()) =', min(prices.values()))  # 最小 value

pair = min(zip(prices.values(), prices.keys()))
print('min(zip(values, keys)) =', pair)                # (最小 value, 對應 key)
