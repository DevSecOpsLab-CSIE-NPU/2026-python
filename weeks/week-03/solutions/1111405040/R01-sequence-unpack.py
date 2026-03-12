"""
R01: 序列拆封（Sequence Unpacking）

這個範例示範「依位置」把序列元素拆到多個變數。
只要左側變數數量與右側元素數量對得上，就可以一次完成指派。
"""

# tuple 會依照順序拆給 x、y。
p = (4, 5)
x, y = p

# list 也可以拆封；第四個欄位本身是一個日期 tuple。
data = ["ACME", 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data

# 巢狀拆封：直接把 date 再拆成 year、mon、day。
name, shares, price, (year, mon, day) = data

# 以底線 _ 當作「不需要此欄位」的慣例名稱。
# 這裡忽略第一欄（name）與第四欄（date），只取 shares、price。
_, shares, price, _ = data
