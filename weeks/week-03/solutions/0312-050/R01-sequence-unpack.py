# R1. 序列解包（1.1）

# 定義一個元組 (tuple) p，包含兩個元素 4 和 5。
p = (4, 5)
# 執行序列解包 (sequence unpacking)。
# 將元組 p 中的第一個元素賦值給變數 x，第二個元素賦值給變數 y。
# 這是 Python 中一種簡潔的賦值方式，可以同時將多個值賦予多個變數。
print(f"原始元組 p: {p}") # 顯示原始元組 p 的內容。
x, y = p
print(f"解包後 x: {x}, y: {y}") # 顯示解包後 x 和 y 的值。

# 定義一個串列 (list) data，包含不同類型的元素：字串、整數、浮點數和一個巢狀元組。
data = ['ACME', 50, 91.1, (2012, 12, 21)]
# 執行序列解包。
# 將串列 data 中的元素依序賦值給 name, shares, price, date 這四個變數。
# 每個變數會對應到串列中相對應位置的元素。
print(f"\n原始串列 data: {data}") # 顯示原始串列 data 的內容。
name, shares, price, date = data
print(f"解包後 name: {name}, shares: {shares}, price: {price}, date: {date}") # 顯示解包後各變數的值。

# 再次執行序列解包，這次針對巢狀元組進行更深層次的解包。
# 將 data 中的前三個元素賦值給 name, shares, price。
# 將 data 中的第四個元素（一個元組 (2012, 12, 21)）進一步解包，將其元素賦值給 year, mon, day。
name, shares, price, (year, mon, day) = data
print(f"深度解包後 name: {name}, shares: {shares}, price: {price}, year: {year}, mon: {mon}, day: {day}") # 顯示深度解包後各變數的值。

# 使用底線 `_` 作為變數名來忽略不關心的元素。
# 這裡只關心 shares 和 price，其他元素則被忽略。
_, shares, price, _ = data
print(f"部分解包並忽略不關心元素後 shares: {shares}, price: {price}") # 顯示部分解包後 shares 和 price 的值。
