# R1. 序列解包（1.1）
#
# 這個範例示範 Python 的「序列解包」：
# 1. 可以把 tuple、list 這類序列直接拆成多個變數。
# 2. 變數數量要和序列中的元素數量對得上。
# 3. 不想接收的值可以用底線 _ 代替，表示刻意忽略。
# 4. 如果序列中還有巢狀資料，也可以在解包時一併拆開。

p = (4, 5)
x, y = p

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
name, shares, price, (year, mon, day) = data

# 丟棄不需要的值（占位）
_, shares, price, _ = data
