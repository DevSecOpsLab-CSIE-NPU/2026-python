# U8. 字典最值為何常用 zip(values, keys)（1.8）

prices = {'A': 2.0, 'B': 1.0}

# 直接對字典做 min，實際上是在比較 key
min_key = min(prices)            # 回傳 key 的最小值（字母序）

# 只看 values 雖然能找到最小值，但不知道它對應哪個 key
min_value = min(prices.values())   # 回傳最小 value，但你不知道是哪個 key

# 把 value 與 key 配對後比較，就能同時取得最小值及其對應鍵
min_pair = min(zip(prices.values(), prices.keys()))
# 回傳 (最小value, 對應key)，一次拿到兩者

print('min(prices) =', min_key)
print('min(prices.values()) =', min_value)
print('min(zip(values, keys)) =', min_pair)
