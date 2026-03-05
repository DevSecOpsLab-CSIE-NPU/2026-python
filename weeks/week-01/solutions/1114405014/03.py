# 03.py - 使用列表、元組、集合和字典並存取元素
numvers = [1, 2, 3, 4, 5]             # 數字列表
point = (3, 4)                         # 表示座標的元組
unique = {1, 2, 3, 4, 5}              # 唯一數字的集合
prices = { 'AAPL': 150.0, 'GOOG': 2800.0, 'MSFT': 300.0 }  # 對應股票價格的字典

numvers.append(4)                      # 將 4 加到列表末尾
first = point[0]                       # 取元組的第一個元素
prices['AAPL']                         # 從字典中取得值

print(numvers)
print(point)
print(unique)
print(prices)
print(numvers)
print(first)
print(prices['AAPL'])