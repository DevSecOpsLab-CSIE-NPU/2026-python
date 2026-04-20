# R8. 字典運算：min/max/sorted + zip（1.8）

# 定義一個字典 prices，儲存股票代碼及其對應的價格。
prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}
# 顯示原始字典內容。
print(f"原始股票價格字典 prices: {prices}\n")

print("--- 使用 zip() 結合值和鍵進行運算 ---")
# 使用 zip() 函式將字典的值 (prices.values()) 和鍵 (prices.keys()) 配對組合。
# 因為 min/max/sorted 在比較元組 (tuple) 時，預設會先比較第一個元素，我們把「價格 (值)」放在前面，這樣就能依價格進行比較。

# 找出價格最低的 (價格, 股票代碼) 組合。
min_price_key = min(zip(prices.values(), prices.keys()))
print(f"最低價格與對應股票 (min + zip): {min_price_key}")

# 找出價格最高的 (價格, 股票代碼) 組合。
max_price_key = max(zip(prices.values(), prices.keys()))
print(f"最高價格與對應股票 (max + zip): {max_price_key}")

# 將股票按價格由低到高排序，回傳一個包含 (價格, 股票代碼) 元組的串列。
sorted_prices = sorted(zip(prices.values(), prices.keys()))
print(f"按價格由低到高排序的股票列表 (sorted + zip):\n  {sorted_prices}\n")

print("--- 使用 key 參數直接在字典上運算 ---")
# 直接對字典使用 min()，這會預設迭代字典的「鍵 (keys)」。
# 透過 key=lambda k: prices[k] 指定比較的依據為「該鍵對應的值 (價格)」。
# 這種寫法只會回傳「鍵 (股票代碼)」，不會包含價格，若需要價格得另外查詢。
min_key_only = min(prices, key=lambda k: prices[k])  # 回傳 key
print(f"價格最低的股票代碼 (min 搭配 key 參數): {min_key_only}")
print(f"該股票的實際價格: {prices[min_key_only]}")
