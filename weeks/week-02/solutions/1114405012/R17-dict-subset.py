# R17. 字典子集（1.17）
#
# 觀念重點：用字典推導式可快速從原字典挑出「符合條件」的子集合。

prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}

# 依 value 篩選：只留下價格大於 200 的項目。
p1 = {k: v for k, v in prices.items() if v > 200}

tech_names = {'AAPL', 'IBM'}

# 依 key 篩選：只留下公司代號在 tech_names 集合中的項目。
p2 = {k: v for k, v in prices.items() if k in tech_names}
