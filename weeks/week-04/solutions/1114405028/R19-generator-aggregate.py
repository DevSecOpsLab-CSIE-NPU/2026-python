# R19. 轉換+聚合：生成器表達式（1.19）

nums = [1, 2, 3]
sum(x * x for x in nums)  # 生成器傳入 sum，不需先建立整個 list，節省記憶體
                           # 等同 sum([1, 4, 9])，但更省記憶體

s = ('ACME', 50, 123.45)
','.join(str(x) for x in s)  # 先將每個元素轉換為字串，再以逗號連接
                              # 結果：'ACME,50,123.45'

portfolio = [{'name': 'AOL', 'shares': 20}, {'name': 'YHOO', 'shares': 75}]
min(s['shares'] for s in portfolio)          # 只取最小的 shares 數值（整數）
min(portfolio, key=lambda s: s['shares'])    # 取 shares 最小的整個 dict 物件
