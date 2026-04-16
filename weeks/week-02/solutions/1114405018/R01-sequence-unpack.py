"""R1. 序列解包（Sequence Unpacking）

這個範例示範 Python 如何把序列中的元素一次拆開，
直接指定給多個變數。這種寫法常見於：
1. tuple / list 的拆解
2. 多層巢狀資料的拆解
3. 丟棄不需要的欄位
"""

# 一個二元 tuple，可以直接拆成兩個變數
p = (4, 5)
# 左邊變數數量要與右邊元素數量一致
x, y = p

# 一個混合型資料：字串、數字、浮點數、以及巢狀 tuple
data = ['ACME', 50, 91.1, (2012, 12, 21)]

# 最外層的四個元素，分別對應到四個變數
name, shares, price, date = data

# 巢狀解包：最後一個元素本身也是 tuple，所以可以再繼續拆成 year / mon / day
name, shares, price, (year, mon, day) = data

# 丟棄不需要的值（占位）
# 底線 _ 是常見慣例，表示這個值雖然有被解包出來，但我們不打算使用它
_, shares, price, _ = data
