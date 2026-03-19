"""
R17: 取出字典的部分資料

示範用字典推導式建立子集合。
"""

prices = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55}

# 只保留價格大於 200 的項目。
p1 = {k: v for k, v in prices.items() if v > 200}

tech_names = {"AAPL", "IBM"}

# 只保留指定名稱的項目。
p2 = {k: v for k, v in prices.items() if k in tech_names}
