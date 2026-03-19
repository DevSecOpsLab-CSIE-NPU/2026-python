# R1. 序列解包（1.1）

p = (4, 5)
x, y = p

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
name, shares, price, (year, mon, day) = data

# 丟棄不需要的值（占位）
_, shares, price, _ = data
