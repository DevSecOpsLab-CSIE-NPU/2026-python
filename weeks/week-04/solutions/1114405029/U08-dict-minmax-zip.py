# U8. 字典最值為何常用 zip(values, keys)（1.8）

# 建立一個字典 prices
# key 代表商品名稱或代號
# value 代表對應的價格
prices = {'A': 2.0, 'B': 1.0}

# 直接對字典使用 min(prices)
# 預設只會比較字典的 key
# 也就是依照 key 的字母序（或數值大小）來找最小值
min_key = min(prices)            # 回傳 key 的最小值（字母序）

# 對 prices.values() 使用 min()
# 可以找出最小的 value
# 但只能知道最小價格是多少，無法直接知道它對應哪一個 key
min_value = min(prices.values())   # 回傳最小 value，但你不知道是哪個 key

# 使用 zip(prices.values(), prices.keys())
# 會把 value 與 key 配對成一組一組的 tuple
# 例如這裡會變成：
# (2.0, 'A')
# (1.0, 'B')
#
# 再對這些 tuple 使用 min()，
# Python 會先比較 tuple 的第一個元素，也就是 value
# 因此可以先找出最小 value，
# 而且結果中還會連同對應的 key 一起回傳
min_pair = min(zip(prices.values(), prices.keys()))
# 回傳 (最小value, 對應key)，一次拿到兩者

# 印出原始字典 prices
print("原始字典 prices：")
print(prices)

print()  # 空一行，讓輸出結果更清楚

# 印出直接對字典使用 min() 的結果
print("min(prices) 的結果：", min_key)
print("說明：這裡比較的是 key，所以回傳的是字母序較小的 key。")

print()  # 空一行，讓輸出結果更清楚

# 印出最小 value 的結果
print("min(prices.values()) 的結果：", min_value)
print("說明：這裡只知道最小的 value 是多少，但無法直接知道它對應哪個 key。")

print()  # 空一行，讓輸出結果更清楚

# 印出使用 zip() 後再取最小值的結果
print("min(zip(prices.values(), prices.keys())) 的結果：", min_pair)
print("說明：這樣可以同時取得最小的 value，以及它對應的 key。")

print()  # 空一行，讓輸出結果更清楚

# 額外把結果拆開印出，讓觀察更清楚
print("最小的 value 是：", min_pair[0])
print("對應的 key 是：", min_pair[1])