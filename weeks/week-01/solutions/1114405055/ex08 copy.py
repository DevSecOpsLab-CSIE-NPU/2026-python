# --- 1. 列表推導式 (List Comprehension) ---
# 從 nums 清單中篩選出大於 0 的數字，並建立一個新清單
nums = [1, -2, 3, -4]
positives = [n for n in nums if n > 0]
print(positives)  # 輸出: [1, 3]

# --- 2. 字典推導式 (Dict Comprehension) ---
# 將包含元組 (Tuple) 的清單轉換成鍵值對 (Key-Value) 的字典格式
pairs = [('a', 1), ('b', 2)]
lookup = {k: v for k, v in pairs}
print(lookup)  # 輸出: {'a': 1, 'b': 2}

# --- 3. 生成器表達式 (Generator Expression) ---
# 直接在 sum() 函式中計算每個數字的平方並加總
# 這裡不使用中括號 [] 可以節省記憶體，因為它不會先產生整個清單
squares_sum = sum(n * n for n in nums)
print(squares_sum)  # 輸出: 30 (計算過程: 1 + 4 + 9 + 16)