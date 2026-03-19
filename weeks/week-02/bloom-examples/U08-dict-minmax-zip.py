# U8. 字典最值為何常用 zip(values, keys)（1.8）

# 實務問題：給定字典 prices，要找最便宜的商品及其代號。
# 難點是：一般 min 無法同時回傳「最小值」和「對應的鍵」。

prices = {'A': 2.0, 'B': 1.0}

# 方式 1：直接 min(prices)
# 此時 min 會比較字典「鍵」，用字典鍵本身的預設順序（通常字母序）。
# 結果：'A'（因為 'A' < 'B' 按字母序）。
# 缺點：回傳的是鍵，完全忽略了值（價格）。
min(prices)            # 回傳 key 的最小值（字母序）

# 方式 2：min(prices.values())
# 此時 min 會比較字典的「值」，回傳最小值。
# 結果：1.0（因為 1.0 < 2.0）。
# 缺點：只知道最小價格，不知道是哪一件商品（丟失鍵的資訊）。
min(prices.values())   # 回傳最小 value，但你不知道是哪個 key

# 方式 3：min(zip(prices.values(), prices.keys()))
# 巧妙之處：
# - zip(prices.values(), prices.keys()) 產生 (value, key) tuple：(2.0, 'A'), (1.0, 'B')
# - Python 比較 tuple 時，先比第一個元素，相同才比第二個。
# - min 會比較 (1.0, 'B') vs (2.0, 'A')，由於 1.0 < 2.0，所以 (1.0, 'B') 最小。
# - 結果：(1.0, 'B')，同時拿到最小價格和對應商品！
#
# 這個技巧常用在需要同時取最值和相關屬性的情境。
min(zip(prices.values(), prices.keys()))
print(min(zip(prices.values(), prices.keys())))
# 回傳 (最小value, 對應key)，一次拿到兩者

# 補充：max 也適用同樣原理
# max(zip(prices.values(), prices.keys())) 會回傳 (2.0, 'A')
