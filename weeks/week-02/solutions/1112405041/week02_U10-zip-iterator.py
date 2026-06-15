# 【Bloom 階段：U - 理解與進階應用】
# U10. zip 的一次性特性地雷 (Iterator Exhaustion)
# August 的惡意提醒：這對應 Week 01 的主題 06。
# 當你對 zip 物件執行一次 min() 後，它就被「耗盡」了！

prices = {'A': 2.0, 'B': 1.0}
z = zip(prices.values(), prices.keys())

# 第一遍遍歷：OK
min_val = min(z)
print(f"Min: {min_val}")

# 第二遍遍歷：會噴 ValueError 或得到空結果
try:
    max_val = max(z)
except ValueError as e:
    print(f"August 的惡意地雷再次觸發：{e}")

# 解決方案：如果需要多次使用，請先轉換為列表 list(z)
print("Tip: Convert zip to list if multiple scans are needed.")
