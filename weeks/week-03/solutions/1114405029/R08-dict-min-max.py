# R8. 字典運算：min/max/sorted + zip（1.8）

# 原始資料：股票名稱與價格
prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}

# ── 使用 zip() 反轉鍵值進行運算 ────────────────────────
# zip(prices.values(), prices.keys()) 會產生一系列的元組，
# 格式如：(45.23, 'ACME'), (612.78, 'AAPL'), (10.75, 'FB')。
# 這樣做的好處是，當執行 min/max/sorted 時，Python 會優先比較元組的第一個元素（價格）。

# 找出價格最低的項目
# 結果：(10.75, 'FB')
min(zip(prices.values(), prices.keys()))

# 找出價格最高的項目
# 結果：(612.78, 'AAPL')
max(zip(prices.values(), prices.keys()))

# 依照價格從小到大進行排序
# 結果：[(10.75, 'FB'), (45.23, 'ACME'), (612.78, 'AAPL')]
sorted(zip(prices.values(), prices.keys()))

# ── 使用 key 參數的另一種方法 ──────────────────────────
# 如果不使用 zip，也可以透過 min() 的 key 參數來指定比較基準。
# 這會回傳「值最小的那個鍵 (Key)」。
# 結果：'FB'
min(prices, key=lambda k: prices[k])  # 僅回傳鍵名，不包含數值