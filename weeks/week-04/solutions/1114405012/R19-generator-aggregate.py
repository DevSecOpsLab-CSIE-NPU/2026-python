# R19. 轉換+聚合：生成器表達式（1.19）
# 生成器表達式可避免中間暫存串列，讓聚合更省記憶體。

nums = [1, 2, 3, 4]

# 直接把生成器丟進 sum，計算平方和。
sum_sq = sum(x * x for x in nums)
print("平方和:", sum_sq)

s = ("ACME", 50, 123.45)

# 先轉字串再 join，常用於輸出 CSV 風格字串。
csv_line = ",".join(str(x) for x in s)
print("tuple 轉 CSV 字串:", csv_line)

portfolio = [
    {"name": "AOL", "shares": 20},
    {"name": "YHOO", "shares": 75},
    {"name": "IBM", "shares": 10},
]

# 只取最小股數數值。
min_shares = min(item["shares"] for item in portfolio)
print("最小 shares 數值:", min_shares)

# 取出 shares 最小的完整字典。
min_item = min(portfolio, key=lambda item: item["shares"])
print("shares 最小的完整項目:", min_item)
