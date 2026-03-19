"""
U08: 字典搭配 min/max 與 zip

只用 min(prices) 會比較 key，不是比較 value。
"""

prices = {"A": 2.0, "B": 1.0}

min(prices)          # 比較 key，結果是 "A"
min(prices.values())  # 只拿到最小 value，無法知道是哪個 key

# 把 value 和 key 綁在一起後，就能同時得到兩者。
min(zip(prices.values(), prices.keys()))
