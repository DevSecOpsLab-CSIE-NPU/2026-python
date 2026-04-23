# 主題 03：基本容器型別 - 簡易教學版

# 基本容器型別（collection types）
numbers = [1, 2, 3]              # list：可變的有序序列（可以新增、刪除、修改）
point = (4, 5)                   # tuple：不可變的有序序列（一旦建立就不能改變）
unique = {1, 2, 3}               # set：無序且不重複的集合（去重複很好用）
prices = {'AAPL': 150.0, 'MSFT': 320.5}  # dict：鍵值對的映射

# list 的基本操作
numbers.append(4)        # 新增元素到 list
first = numbers[0]       # 取得 list 的第一個元素
print(f"List: {numbers}, 第一個元素: {first}")

# tuple 的基本操作
print(f"Tuple: {point}, 第一個元素: {point[0]}")

# set 的基本操作
unique.add(4)            # 新增元素到 set
print(f"Set: {unique}")

# dict 的基本操作
aapl_price = prices['AAPL']  # 用 key 來取得 value
prices['GOOGL'] = 2800.0     # 新增鍵值對
print(f"Dict: {prices}")
print(f"AAPL 價格: {aapl_price}")
