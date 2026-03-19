# R17. 字典子集（1.17）
# 此程式示範如何使用字典推導式（dictionary comprehension）來創建字典的子集。
# 字典推導式類似於列表推導式，但用於創建新的字典。
# 語法：{key_expression: value_expression for item in iterable if condition}

# 定義一個字典 prices，鍵是股票代碼，值是對應的價格
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}

# 使用字典推導式創建 p1，只包含價格大於 200 的項目
# 這裡的條件是 v > 200，其中 v 是價格值
# 結果：p1 將包含 'AAPL': 612.78 和 'IBM': 205.55
p1 = {k: v for k, v in prices.items() if v > 200}

# 定義一個集合 tech_names，包含技術公司的股票代碼
# 集合用於快速檢查成員資格
tech_names = {'AAPL', 'IBM'}

# 使用字典推導式創建 p2，只包含鍵在 tech_names 中的項目
# 這裡的條件是 k in tech_names，其中 k 是股票代碼
# 結果：p2 將包含 'AAPL': 612.78 和 'IBM': 205.55
p2 = {k: v for k, v in prices.items() if k in tech_names}
