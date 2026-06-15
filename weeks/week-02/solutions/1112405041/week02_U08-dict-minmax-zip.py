# 【Bloom 階段：U - 理解與進階應用】
# U8. 為什麼字典尋找極值推薦用 zip(values, keys)？
# August 的惡意提醒：這是面試常考的陷阱題。

prices = {'A': 2.0, 'B': 1.0}

# 1. 錯誤示範：直接 min()
# 結果會是 'A'，因為它是在比 Key 的字串大小
print(f"min(prices) results in key compare: {min(prices)}")

# 2. 局部正確：min(values)
# 雖然能拿到 1.0，但你不知道是誰賣這個價錢
print(f"min(prices.values()) loses key info: {min(prices.values())}")

# 3. 完美示範：zip(values, keys)
# 利用 Tuple 逐項比較的特性，先比數值，再比鍵名
min_val_key = min(zip(prices.values(), prices.keys()))
print(f"zip logic returns both: {min_val_key}") # (1.0, 'B')
