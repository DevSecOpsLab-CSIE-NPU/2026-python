"""R01: 序列解包 (sequence unpacking) 範例。"""

# tuple 解包
p = (4, 5)
x, y = p
print('tuple 解包:', x, y)

# 巢狀解包
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, (year, month, day) = data
print('名稱/股數/價格:', name, shares, price)
print('日期:', year, month, day)

# 忽略不需要的欄位 (慣例用 _)
_, shares2, price2, _ = data
print('只取股數與價格:', shares2, price2)
