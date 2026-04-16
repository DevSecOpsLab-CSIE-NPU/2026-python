"""R11. 命名切片 slice（1.11）

這個範例示範如何使用 slice 物件為固定位置的欄位命名。
這樣做的好處：
1. 程式可讀性更高，不必一直看魔術數字。
2. 欄位位置若修改，只要改一個地方就好。
3. 常用在處理固定格式文字、紀錄檔、欄位資料。
"""

# 固定格式字串：每個欄位的位置已經事先安排好
record = '....................100 .......513.25 ..........'

# 用 slice 物件把欄位位置命名，讓程式更容易理解
SHARES = slice(20, 23)
PRICE = slice(31, 37)

# 先取出 shares 欄位轉成整數，再取出 price 欄位轉成浮點數並相乘
# record[SHARES] 等價於 record[20:23]
# record[PRICE] 等價於 record[31:37]
cost = int(record[SHARES]) * float(record[PRICE])
