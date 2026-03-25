# ============================================================================
# R8. 字典的最值運算 - min/max/sorted 與 zip（1.8）
# ============================================================================
# 本題展示如何高效地從字典中取得最小/最大的鍵或值。
# 核心技巧：使用 zip(values, keys) 巧妙地配對。
# ============================================================================

print("【場景】在股票投資組合中找最便宜和最貴的股票\n")

prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}
print(f"股票價格：{prices}\n")

print("=" * 50)
print("【方法 1】min/max(prices) - 只返回鍵")
print("=" * 50)
print()

min_key = min(prices)  # 按鍵大小比較
max_key = max(prices)  # 字母序

print(f"min(prices) = {repr(min_key)}  （最小鍵）")
print(f"max(prices) = {repr(max_key)}  （最大鍵）")
print()
print("問題：這不是我們要的！")
print("  - 我們要的是最低價和最高價")
print("  - 而不是字母序最小/最大的鍵\n")

print("=" * 50)
print("【方法 2】min/max(prices.values()) - 只返回值")
print("=" * 50)
print()

min_price = min(prices.values())  # 10.75
max_price = max(prices.values())  # 612.78

print(f"min(prices.values()) = {min_price}")
print(f"max(prices.values()) = {max_price}")
print()
print("問題：我們得到了價格，但不知道是哪支股票！\n")

print("=" * 50)
print("【方法 3】zip(values, keys) - 完美方案 ✓")
print("=" * 50)
print()

print("代碼：")
print("  min(zip(prices.values(), prices.keys()))")
print("  max(zip(prices.values(), prices.keys()))\n")

min_entry = min(zip(prices.values(), prices.keys()))
max_entry = max(zip(prices.values(), prices.keys()))

print(f"結果：")
print(f"  最便宜：{min_entry[0]}  股票：{min_entry[1]}")
print(f"  最貴：  {max_entry[0]}  股票：{max_entry[1]}")
print()

print("說明：")
print("  - zip 將鍵和值配對")
print("  - min/max 自動按第一個元素（價格）比較")
print("  - 返回完整信息（價格, 股票代碼）\n")

print("=" * 50)
print("【方法 4】sorted 取全部")
print("=" * 50)
print()

sorted_prices = sorted(zip(prices.values(), prices.keys()))
print(f"sorted(zip(prices.values(), prices.keys())) = ")
for price, stock in sorted_prices:
    print(f"  ({price:7.2f}, {stock})")
print()

print("說明：")
print("  - 從便宜到貴排序")
print("  - 看起來 FB 最便宜，AAPL 最貴\n")

print("=" * 50)
print("【方法 5】key 參數 - 對單一字典")
print("=" * 50)
print()

print("代碼：")
print("  min(prices, key=lambda k: prices[k])")
print()

min_stock = min(prices, key=lambda k: prices[k])
max_stock = max(prices, key=lambda k: prices[k])

print(f"結果：")
print(f"  最便宜股票：{min_stock}  價格 {prices[min_stock]}")
print(f"  最貴股票：{max_stock}  價格 {prices[max_stock]}")
print()

print("說明：")
print("  - 使用 key 參數提取比較用的值")
print("  - 返回鍵（股票代碼）\n")

print("=" * 50)
print("【效能比較】")
print("=" * 50)
print("""
dict = {'a': 1, 'b': 2, ...}  (100 個元素)

min(dict)                      速度：快   結果：鍵
min(dict.values())             速度：快   結果：值
min(zip(dict.values(), dict))  速度：中   結果：(值, 鍵) ✓
min(dict, key=lambda k: dict[k]) 速度：快  結果：鍵

推薦：
  ✓ 只要鍵 → min(dict)
  ✓ 只要值 → min(dict.values())
  ✓ 要鍵和值 → min(zip(values, keys))
  ✓ 複雜比較 → key 參數
""")
