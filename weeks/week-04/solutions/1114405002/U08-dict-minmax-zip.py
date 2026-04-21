# U08 字典取最值時的常見陷阱
# 重點：min(dict) 比的是 key，不是 value。

prices = {"A": 2.0, "B": 1.0}

# 1) 這行比較的是 key（字典鍵）。
min(prices)

# 2) 這行回傳最小 value，但你拿不到對應 key。
min(prices.values())

# 3) 將 (value, key) 配對後取最小，可同時得到 value 與 key。
min(zip(prices.values(), prices.keys()))
