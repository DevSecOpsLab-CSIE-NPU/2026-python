# R1. 序列解包（1.1）

# 將 tuple 中的兩個值分別解包到 x、y
p = (4, 5)
x, y = p

# 一次解包多個欄位
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data

# 巢狀解包：直接把 date 再拆成 year、mon、day
name, shares, price, (year, mon, day) = data

# 丟棄不需要的值（慣例用 _ 當占位符）
_, shares, price, _ = data
