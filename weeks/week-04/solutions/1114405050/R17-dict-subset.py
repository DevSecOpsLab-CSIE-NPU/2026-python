# R17. 字典子集（1.17）
"""
本範例示範如何從一個字典中建立「子集」。

主要技術：
- 字典推導式（dictionary comprehension）
- 運用條件過濾來選擇符合需求的鍵值對

常見用途：
- 從大量資料中擷取符合條件的子集
- 根據某些欄位或篩選條件製作新字典
"""

# 範例資料：股票代碼到價格的對應
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}

# 方法一：根據值過濾
# 這裡只保留價格大於 200 的股票
# 推導式語法：{k: v for k, v in prices.items() if v > 200}
# prices.items() 會回傳 (key, value) 的迭代對，k 對應 key，v 對應 value
p1 = {k: v for k, v in prices.items() if v > 200}

# 方法二：根據鍵過濾
# 定義要保留的股票代碼集合
tech_names = {'AAPL', 'IBM'}

# 只保留 key (股票代碼) 在 tech_names 集合中的項目
# 這裡的條件是 k in tech_names
p2 = {k: v for k, v in prices.items() if k in tech_names}
