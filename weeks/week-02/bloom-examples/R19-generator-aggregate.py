# R19. 轉換+聚合：生成器表達式（1.19）

# 一組數字資料。
nums = [1, 2, 3]

# 生成器表達式搭配 sum：
# 先逐一把每個 x 轉成 x*x，再做總和。
# 這裡結果是 1^2 + 2^2 + 3^2 = 14。
#
# 寫成生成器（而非先建 list）可避免中間清單的額外記憶體配置。
sum(x * x for x in nums)

# 一個包含不同型別元素的 tuple（字串、整數、浮點數）。
s = ('ACME', 50, 123.45)

# join 只能串接「字串」，因此先用 str(x) 逐項轉字串。
# 生成器表達式會在 join 需要時才產生下一個字串。
# 結果字串為：'ACME,50,123.45'
','.join(str(x) for x in s)

# 模擬投資組合資料：每筆是 dict，含股票名稱與持股數。
portfolio = [{'name': 'AOL', 'shares': 20}, {'name': 'YHOO', 'shares': 75}]

# 先把每筆資料的 shares 抽出來，再取最小值。
# 此寫法回傳的是最小的「數值」，結果為 20。
min(s['shares'] for s in portfolio)

# 直接對整筆資料取最小值，透過 key 指定比較依據為 shares。
# 此寫法回傳的是「整筆 dict」，例如 {'name': 'AOL', 'shares': 20}。
#
# 總結：
# - min(... for ...): 回傳比較值本身
# - min(iterable, key=...): 回傳原始元素
min(portfolio, key=lambda s: s['shares'])
