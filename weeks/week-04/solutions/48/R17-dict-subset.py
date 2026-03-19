# R17. 字典子集（1.17）
# 展示如何使用字典推導式建立字典的子集

# 原始字典：股票名稱和價格
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}

# 方法 1：根據值的條件篩選
# 只保留價格超過 200 的股票
p1 = {k: v for k, v in prices.items() if v > 200}
print("方法 1 - 根據值篩選:", p1)  # 結果：{'AAPL': 612.78, 'IBM': 205.55}

# 定義目標股票集合
tech_names = {'AAPL', 'IBM'}

# 方法 2：根據鍵的條件篩選
# 只保留在 tech_names 集合中的股票
p2 = {k: v for k, v in prices.items() if k in tech_names}
print("方法 2 - 根據鍵篩選:", p2)  # 結果：{'AAPL': 612.78, 'IBM': 205.55}
