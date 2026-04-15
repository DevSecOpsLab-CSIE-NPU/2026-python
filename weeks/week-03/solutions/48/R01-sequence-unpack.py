# R1. 序列解包（1.1）

p = (4, 5)
# 將 tuple 依序解包到兩個變數
x, y = p

data = ['ACME', 50, 91.1, (2012, 12, 21)]
# 依照位置把串列內容解包到對應變數
name, shares, price, date = data
# 巢狀解包：第四個元素本身也是 tuple，可再往內拆開
name, shares, price, (year, mon, day) = data

# 丟棄不需要的值（占位）
# 慣例使用 _ 表示「這個值我不會用到」
_, shares, price, _ = data
