# 04.py - 使用迴圈計算總和並建立新的列表
items = [2, 4, 6]

total = 0
for x in items:
    total += x              # 累加元素值

squares = []
for x in items:
    squares.append(x * x)   # 對每個元素平方並加入列表

print(f"items = {items}")
print(f"total = {total}  # 所有項目的和")

print(f"squares = {squares}  # 每個項目的平方")