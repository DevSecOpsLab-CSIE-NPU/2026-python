# R17. 字典子集（1.17）

# 原始資料：股票代號 -> 股價。
# 目標是從既有字典中，依條件挑出「子集合」形成新字典。
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}

# 子集做法 1：依「值（股價）」過濾。
# 字典推導式格式：{新鍵: 新值 for 鍵, 值 in 可迭代資料 if 條件}
# 這裡條件是 v > 200，所以只留下高於 200 的股票。
# 結果預期：{'AAPL': 612.78, 'IBM': 205.55}
p1 = {k: v for k, v in prices.items() if v > 200}
print(p1)

# 先定義一組想保留的股票代號。
# 使用 set（集合）做 membership 測試通常更有效率，
# 判斷 k in tech_names 的平均時間複雜度約為 O(1)。
tech_names = {'AAPL', 'IBM'}

# 子集做法 2：依「鍵（股票代號）」過濾。
# 只要鍵存在於 tech_names 集合，就把該鍵值對放入新字典。
# 結果預期同樣為：{'AAPL': 612.78, 'IBM': 205.55}
p2 = {k: v for k, v in prices.items() if k in tech_names}
print(p2)