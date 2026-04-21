# R19 生成器搭配聚合函式
# 主題：sum/min/join 與 generator expression 的常見組合

nums = [1, 2, 3]

# 1) 不建立中間清單，直接逐項平方後加總。
sum(x * x for x in nums)

s = ("ACME", 50, 123.45)

# 2) join 只能接字串，因此先轉型。
",".join(str(x) for x in s)

portfolio = [{"name": "AOL", "shares": 20}, {"name": "YHOO", "shares": 75}]

# 3) 只取最小 shares 值。
min(stock["shares"] for stock in portfolio)

# 4) 直接取最小 shares 的整筆資料。
min(portfolio, key=lambda stock: stock["shares"])
