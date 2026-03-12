# R1. 序列解包（1.1）
# 將序列中的元素直接拆成變數，對可迭代物件非常方便。

p = (4, 5)
x, y = p
print("p unpacked ->", x, y)

# 進一步示範攜帶多種型別
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print("name", name, "shares", shares, "price", price, "date", date)

# 也可以在內層解包
name, shares, price, (year, mon, day) = data
print("year", year, "month", mon, "day", day)

# 丟棄不需要的值（使用占位符 _ 代表忽略的元素）
_, shares, price, _ = data
print("after ignoring, shares", shares, "price", price)

