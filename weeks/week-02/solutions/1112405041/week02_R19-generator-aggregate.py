# 【Bloom 階段：R - 記憶與基本操作】
# R19. 同時轉換並縮減數據 (Generator Aggregation)
# August 的惡意提醒：不要寫出 sum([x*x for x in nums])。
# 注意那個中括號！加上中括號會產生一個臨時列表，浪費內存。
# 直接在 sum() 內寫推導式，Python 會將其視為生成器，這才是 O(1) 空間的指紋。

nums = [1, 2, 3, 4, 5]
# 推薦做法：不加中括號，使用生成器表達式
sum_sq = sum(x * x for x in nums)

# 處理複雜結構
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20}
]

# 找出持有股數最少的那家 (利用 lambda 或 generator)
min_shares_val = min(s['shares'] for s in portfolio)
min_shares_obj = min(portfolio, key=lambda s: s['shares'])

print(f"Squares Sum: {sum_sq}")
print(f"Min Shares Value: {min_shares_val}")
print(f"Min Shares Stock: {min_shares_obj['name']}")
