# R8. 字典運算：min/max/sorted + zip（1.8）
# 本程式示範如何在字典上執行 min、max 和 sorted 運算
# 特別是使用 zip 函數將字典的值和鍵配對，以便根據值進行比較
# 這對於處理字典數據時需要根據值排序或找到極值的情況很有用

# 定義一個字典 prices，包含股票代號作為鍵，對應的價格作為值
# 這是一個簡單的字典，用來模擬股票價格數據
prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}

# 使用 zip 函數將 prices.values()（價格值）和 prices.keys()（股票代號）配對成元組列表
# zip 會將對應位置的元素配對，例如：[(45.23, 'ACME'), (612.78, 'AAPL'), (10.75, 'FB')]
# 然後使用 min() 函數找到價格最小的配對元組
# 由於元組的第一個元素是價格，min 會根據價格比較，返回價格最低的元組
min(zip(prices.values(), prices.keys()))

# 同樣地，使用 max() 函數找到價格最高的配對元組
# max 會根據元組的第一個元素（價格）進行比較，返回價格最高的元組
max(zip(prices.values(), prices.keys()))

# 使用 sorted() 函數對配對的元組列表進行排序
# sorted 會根據元組的第一個元素（價格）從小到大排序，返回排序後的列表
sorted(zip(prices.values(), prices.keys()))

# 使用 min() 函數直接在字典鍵上操作，並指定 key 參數
# key=lambda k: prices[k] 表示比較的依據是鍵對應的值（價格）
# 這樣會找到價格最小的鍵，並返回該鍵（而不是值）
min(prices, key=lambda k: prices[k])  # 回傳 key
