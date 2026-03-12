# R01 sequence unpack
# 目標：示範 Python 序列解包，以及如何丟棄不需要的欄位。

p = (4, 5)
# 將 tuple 的兩個值一次解包到 x、y
x, y = p

# 常見的資料列：名稱、股數、價格、日期
data = ["ACME", 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data

# 巢狀解包：直接取出年、月、日
name, shares, price, (year, mon, day) = data

# 用 _ 當占位，表示該值不打算使用
_, shares, price, _ = data
