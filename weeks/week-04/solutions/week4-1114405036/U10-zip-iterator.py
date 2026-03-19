# U10. zip 為何只能用一次（範例 1.8）
# 原理：zip 回傳的是一個迭代器 (iterator)。迭代器被走訪過一次後就「乾涸」了，無法重複使用。

prices = {'A': 2.0, 'B': 1.0}
z = zip(prices.values(), prices.keys())

min_val = min(z) # OK，但此時 z 已經被消耗完了
# max_val = max(z) # 這裡會出錯或回傳空，因為 z 已空。