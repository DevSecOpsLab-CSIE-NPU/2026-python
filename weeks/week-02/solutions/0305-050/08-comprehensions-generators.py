# 8 容器操作與推導式範例 (Container Operations and Comprehensions Examples)

# 定義一個包含整數的串列 (List)，其中包含正數與負數。
nums = [1, -2, 3, -4]

# 使用「串列推導式 (List Comprehension)」來過濾資料。
# 這裡的邏輯是：走訪 nums 迴圈中的每一個數字 n，如果 n 大於 0 (條件判斷 `if n > 0`)，就將它收集起來建立一個新的串列。
# 執行結果 positives 將會是：[1, 3]
positives = [n for n in nums if n > 0]

# 定義一個包含多個元組 (Tuple) 的串列，每個元組包含兩個元素，代表一組配對。
pairs = [('a', 1), ('b', 2)]

# 使用「字典推導式 (Dictionary Comprehension)」將包含元組的串列轉換為字典。
# 這裡的邏輯是：走訪 pairs 串列，將每一個元組解包 (Unpack) 分配給變數 k (鍵) 和 v (值)，並根據 {k: v} 的語法建立字典。
# 執行結果 lookup 將會是：{'a': 1, 'b': 2}
lookup = {k: v for k, v in pairs}

# 轉換與聚合：生成器表達式 (Generator Expression)
# 這裡結合了內建函式 sum() 與生成器表達式 (n * n for n in nums) 來計算 nums 中每個數字的平方和。
# 生成器表達式與串列推導式非常像，但它使用的是小括號 `()`。它不會一次性在記憶體中產生完整的串列，而是「要一個算一個」(惰性求值，Lazy Evaluation)。這在處理龐大資料時，能大幅節省記憶體空間。
squares_sum = sum(n * n for n in nums)
