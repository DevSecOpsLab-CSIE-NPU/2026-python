# R1. 序列解包（1.1）

p = (4, 5)
# 將元組 p 的兩個元素依序解包到變數 x、y
x, y = p

data = ['ACME', 50, 91.1, (2012, 12, 21)]
# 將列表 data 的四個元素依序解包到四個變數
name, shares, price, date = data

# 也可以在解包時進一步解開內部的元組
name, shares, price, (year, mon, day) = data

# 丟棄不需要的值（使用底線 _ 作為占位符）
# 這裡只保留 shares 和 price，其餘位置用 _ 忽略
_, shares, price, _ = data