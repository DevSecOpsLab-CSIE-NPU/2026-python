# R17 字典子集合擷取
# 重點：dict comprehension 可同時過濾鍵與值。

prices = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55}

# 1) 依 value 條件過濾。
p1 = {k: v for k, v in prices.items() if v > 200}

# 2) 依 key 是否屬於指定集合過濾。
tech_names = {"AAPL", "IBM"}
p2 = {k: v for k, v in prices.items() if k in tech_names}
