# R11. 命名切片 slice（1.11）
# 用於固定欄位文字串的抽取，避免硬編號。

record = '....................100 .......513.25 ..........'
SHARES = slice(20, 23)
PRICE = slice(31, 37)
print("record", record)
print("shares substring", record[SHARES])
print("price substring", record[PRICE])
cost = int(record[SHARES]) * float(record[PRICE])
print("computed cost", cost)

