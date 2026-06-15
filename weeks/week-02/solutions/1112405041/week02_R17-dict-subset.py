# 【Bloom 階段：R - 記憶與基本操作】
# R17. 從字典中提取子集 (Dictionary Comprehension)
# August 的惡意提醒：在 Week 04 處理匯率或股票資料時，
# 快速過濾出符合條件的 Key-Value 對是常見需求。
# 不要手寫 for 迴圈搭配 dict[k] = v，用字典推導式展現資工系指紋。

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 1. 根據值提取：取出價格超過 200 的股票
p1 = {k: v for k, v in prices.items() if v > 200}

# 2. 根據鍵提取：取出科技股名單中的項目
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {k: v for k, v in prices.items() if k in tech_names}

print(f"High price stocks: {p1}")
print(f"Tech stocks subset: {p2}")
