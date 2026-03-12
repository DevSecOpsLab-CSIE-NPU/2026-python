# R8. 字典運算：min/max/sorted + zip（Calculating with Dictionaries）—— Python Cookbook 1.8

prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}

# ── 技巧：用 zip 把 values 和 keys 配對後再比較 ────────────
# zip(prices.values(), prices.keys()) 產生 (value, key) 的配對
# 比較時先比 value，value 相同才比 key（字典序）
# 這樣就能「以 value 為主鍵」做 min/max/sorted

min(zip(prices.values(), prices.keys()))
# → (10.75, 'FB')  — 最便宜的股票

max(zip(prices.values(), prices.keys()))
# → (612.78, 'AAPL')  — 最貴的股票

sorted(zip(prices.values(), prices.keys()))
# → [(10.75, 'FB'), (45.23, 'ACME'), (612.78, 'AAPL')]  — 由低到高排序

# ── 方法二：lambda 直接對 key 排序（只回傳 key，不含 value）──
# key=lambda k: prices[k] 以該 key 對應的 value 作為排序依據
# 只想知道「哪家公司最便宜」時較簡潔
min(prices, key=lambda k: prices[k])   # → 'FB'
