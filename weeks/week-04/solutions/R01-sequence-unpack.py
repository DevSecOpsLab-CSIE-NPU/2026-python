# R1. 序列解包（1.1）
# 序列解包（Sequence Unpacking）是 Python 的一個強大功能，
# 允許將一個序列（如元組、列表或字串）的元素直接賦值給多個變數。
# 這使得代碼更加簡潔和可讀。

# 創建一個包含兩個元素的元組 p
p = (4, 5)

# 將元組 p 的元素解包到變數 x 和 y 中
# 這相當於 x = p[0], y = p[1]
x, y = p

# 創建一個列表 data，包含股票名稱、股份數、價格和日期
data = ['ACME', 50, 91.1, (2012, 12, 21)]

# 將列表 data 的元素解包到對應的變數中
# name 獲取 'ACME'，shares 獲取 50，price 獲取 91.1，date 獲取 (2012, 12, 21)
name, shares, price, date = data

# 進行嵌套解包，將日期元組進一步解包
# 這裡將 data 的第四個元素（日期元組）進一步解包到 year, mon, day
name, shares, price, (year, mon, day) = data

# 丟棄不需要的值（占位）
# 有時我們不需要序列中的所有元素，可以使用下劃線 _ 作為占位符來忽略它們
# 這裡忽略了第一個元素（名稱）和第四個元素（日期），只保留 shares 和 price
_, shares, price, _ = data
