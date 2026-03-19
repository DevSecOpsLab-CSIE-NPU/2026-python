# R17. 字典子集（1.17）

# 建立一個字典 prices
# 字典中的 key 代表股票代號
# 字典中的 value 代表該股票的價格
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}

# 使用字典推導式（dictionary comprehension）
# 從 prices.items() 中逐一取出 key 與 value
# 條件是只保留價格大於 200 的項目
# 最後會建立一個新的字典 p1
p1 = {k: v for k, v in prices.items() if v > 200}

# 建立一個集合 tech_names
# 這個集合中放的是我們想要篩選出的股票代號
# 也就是只想保留 AAPL 與 IBM 這兩筆資料
tech_names = {'AAPL', 'IBM'}

# 再次使用字典推導式
# 從 prices.items() 中逐一取出每一組 key 與 value
# 條件是 key 必須存在於 tech_names 集合中
# 符合條件的資料會被放入新的字典 p2
p2 = {k: v for k, v in prices.items() if k in tech_names}

# 印出原始字典 prices
print("原始的股票價格字典 prices：")
print(prices)

print()  # 空一行，讓輸出結果更清楚

# 印出價格大於 200 的字典子集 p1
print("價格大於 200 的字典子集 p1：")
print(p1)

print()  # 空一行，讓輸出結果更清楚

# 印出指定股票名稱的集合 tech_names
print("指定要篩選的股票代號集合 tech_names：")
print(tech_names)

print()  # 空一行，讓輸出結果更清楚

# 印出股票代號存在於 tech_names 中的字典子集 p2
print("股票代號屬於 tech_names 的字典子集 p2：")
print(p2)