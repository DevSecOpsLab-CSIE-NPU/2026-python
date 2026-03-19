# U10. zip 為何只能用一次（1.8）

prices = {'A': 2.0, 'B': 1.0}
z = zip(prices.values(), prices.keys())
# zip 回傳的是「迭代器（iterator）」，不是 list
# 迭代器只能單向遇歷一次，用完即空了

min(z)  # OK：消耗迭代器，回傳 (1.0, 'B')
# max(z)  # 失敗：z 已耗盡，沒有任何元素可比較 -> ValueError

# 若需要多次使用，應先轉成 list：
z_list = list(zip(prices.values(), prices.keys()))  # 就能多次操作
