# R8. 字典運算：min/max/sorted + zip（1.8）
#
# 這份程式示範兩種「找字典極值」技巧：
# 1) 把 (value, key) 配對後再做 min/max/sorted
# 2) 直接對 key 做 min(..., key=...)，比較依據改成 value

# 股票價格字典：key=股票代號, value=價格
prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}


# zip(prices.values(), prices.keys()) 會產生 (value, key) 配對：
# (45.23, 'ACME'), (612.78, 'AAPL'), (10.75, 'FB')
#
# min(...) 會先比 tuple 第一個元素（value），所以可找到最低價對應項目
# 回傳的是整個 tuple，而不是只有 key
min(zip(prices.values(), prices.keys()))

# max(...) 同理，先比 value，找出最高價對應項目
max(zip(prices.values(), prices.keys()))

# sorted(...) 會依 tuple 排序（先 value 再 key）
# 因此會得到按價格由小到大排列的 (value, key) 清單
sorted(zip(prices.values(), prices.keys()))


# 另一種常見寫法：直接在 key 上找最小值
# min(prices, key=...) 代表：
# - 迭代對象是 prices 的 key（'ACME', 'AAPL', 'FB'）
# - 比較規則改用 prices[k]（也就是價格）
# 所以最後回傳的是「key」，不是 value 或 tuple
min(prices, key=lambda k: prices[k])  # 回傳 key


# 讀懂這份程式的步驟：
# 1. 先問自己：我要的結果是 key、value，還是 (value, key) 配對？
# 2. 若要同時保留價值與代號，用 zip(values, keys) 很直觀。
# 3. 若只要「哪個 key 最小/最大」，用 min/max + key= 通常最簡潔。
# 4. 注意這些呼叫若沒接變數，結果只會被計算，不會保留。
