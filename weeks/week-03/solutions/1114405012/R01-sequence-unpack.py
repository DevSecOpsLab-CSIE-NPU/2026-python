# R1. 序列解包（1.1）

# 兩個元素的 tuple 解包成兩個變數
p = (4, 5)
x, y = p
print('x =', x, ', y =', y)

# 較長資料：公司名稱、股數、價格、日期 tuple
data = ['ACME', 50, 91.1, (2012, 12, 21)]

# 一次解出四個欄位
name, shares, price, date = data
print('完整解包:', name, shares, price, date)

# 巢狀解包：直接把日期再拆成年月日
name, shares, price, (year, mon, day) = data
print('巢狀解包日期:', year, mon, day)

# 丟棄不需要的值（占位）
_, keep_shares, keep_price, _ = data
print('只保留股數與價格:', keep_shares, keep_price)
