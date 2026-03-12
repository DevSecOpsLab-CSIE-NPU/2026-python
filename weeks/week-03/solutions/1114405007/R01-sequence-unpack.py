# R1: 序列解包（Sequence Unpacking）
# 觀念：把「可迭代物件」中的元素，按照位置一次指派給多個變數。

p = (4, 5)
# 將 tuple 的第 1、2 個元素分別指派給 x、y
x, y = p

# data 內含字串、整數、浮點數、以及一個日期 tuple
data = ['ACME', 50, 91.1, (2012, 12, 21)]

# 基本解包：依照位置取值
name, shares, price, date = data

# 巢狀解包：直接把 date 這個 tuple 再拆成 year, mon, day
name, shares, price, (year, mon, day) = data

# 若某些欄位暫時不需要，可用 _ 當作「占位符」忽略該值
_, shares, price, _ = data
