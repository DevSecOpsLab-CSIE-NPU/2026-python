# R11. 命名切片 slice（1.11）
#
# slice 可以把固定位置切片命名起來：
# 1. 讓魔術數字變得有意義，程式更容易讀。
# 2. 對固定格式的字串資料很方便。
# 3. 後續若欄位位置改變，只要改 slice 定義即可。

record = '....................100 .......513.25 ..........'
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
