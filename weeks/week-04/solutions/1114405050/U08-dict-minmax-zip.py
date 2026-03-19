# U8. 字典最值為何常用 zip(values, keys)（1.8）
"""
本範例說明如何從 dict 中同時取得「最小（或最大）值」以及對應的 key。

一般情況下：
- 直接對 dict 取 min/max 只會比較 key（因為 dict 的迭代預設是 key）
- 對 dict.values() 取 min/max 可以得到最小/最大值，但無法知道該值對應的 key

因此常見的做法是將 values 和 keys 打包（zip）成 (value, key) 的對，
然後再對這個迭代器取 min/max，就可以一次拿到「值&對應的鍵」。

備註：也可以用 min(prices.items(), key=lambda kv: kv[1]) 取得同樣結果。
"""

prices = {'A': 2.0, 'B': 1.0}

# 1) 直接對 dict 取 min：比較的是 key，結果是字母序最小的 key
min(prices)            # 回傳 key 的最小值（字母序）

# 2) 對 values 取 min：取得最小 value，但不知道它對應的 key 是哪個
min(prices.values())   # 回傳最小 value，但你不知道是哪個 key

# 3) 將 values 與 keys zip 起來，建立 (value, key) 的元組
#    這樣 min() 會先比較 value，再比較 key（若 value 相同）
min(zip(prices.values(), prices.keys()))
# 回傳 (最小value, 對應key)，一次拿到兩者
