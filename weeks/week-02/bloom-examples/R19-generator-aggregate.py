"""
R19: generator 搭配聚合函式

示範 sum、join、min 等函式如何直接接 generator。
"""

nums = [1, 2, 3]

# 不必先建立中間串列。
sum(x * x for x in nums)

s = ("ACME", 50, 123.45)
",".join(str(x) for x in s)

portfolio = [{"name": "AOL", "shares": 20}, {"name": "YHOO", "shares": 75}]

# 只拿 shares 欄位做比較。
min(s["shares"] for s in portfolio)

# 或是直接找出 shares 最小的整筆資料。
min(portfolio, key=lambda s: s["shares"])
