# U8. 字典最值為何常用 zip(values, keys)（1.8）
#
# 觀念重點：
# - 直接對 dict 用 min/max，預設比的是 key。
# - 對 values 用 min/max 雖能拿到值，但會失去 key 資訊。
# - 用 zip(values, keys) 可把 value 與 key 綁在一起一起比較。

prices = {'A': 2.0, 'B': 1.0}

# 預設比較 key（字母序），不是比較價格。
min(prices)

# 只拿到最小 value，但不知道是哪個股票代號。
min(prices.values())

# 回傳 (最小value, 對應key)，一次取得兩者。
min(zip(prices.values(), prices.keys()))
