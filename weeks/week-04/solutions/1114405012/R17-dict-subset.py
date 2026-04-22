# R17. 字典子集（1.17）
# 核心技巧：用字典推導式快速建立「符合條件」的新字典。

prices = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55, "HPQ": 37.2}

# 依 value 篩選：挑出價格大於 200 的股票。
p1 = {k: v for k, v in prices.items() if v > 200}
print("原始價格表:", prices)
print("價格 > 200 的子集:", p1)

tech_names = {"AAPL", "IBM", "MSFT"}

# 依 key 篩選：只留下 tech_names 裡有列到的股票。
# 注意：若 key 不存在於 prices（如 MSFT），不會報錯，會自然被略過。
p2 = {k: v for k, v in prices.items() if k in tech_names}
print("指定公司名稱集合:", tech_names)
print("按名稱過濾的子集:", p2)
