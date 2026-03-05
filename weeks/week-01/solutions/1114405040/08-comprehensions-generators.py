# 8 容器操作與推導式範例
# 本範例展示 Python 中列表推導式、字典推導式和生成器表達式的使用方法

# ========== 列表推導式 (List Comprehension) ==========
# 定義一個包含正數和負數的列表
nums = [1, -2, 3, -4]

# 列表推導式：使用簡潔的語法從 nums 中篩選出所有正數 (大於 0 的數字)
# 語法架構: [expression for item in iterable if condition]
# 結果: positives = [1, 3]
positives = [n for n in nums if n > 0]


# ========== 字典推導式 (Dictionary Comprehension) ==========
# 定義包含鍵值對的元組列表
pairs = [('a', 1), ('b', 2)]

# 字典推導式：將元組列表轉換為字典
# 語法架構: {key_expression: value_expression for item in iterable}
# 結果: lookup = {'a': 1, 'b': 2}
lookup = {k: v for k, v in pairs}


# ========== 生成器表達式 (Generator Expression) ==========
# 生成器表達式與列表推導式類似，但使用圓括號 () 而非方括號 []
# 優點：節省記憶體，適合一次性迭代大型數據集

# 計算所有數字的平方和 (每個數字乘以自己再相加)
# sum() 函數對生成器表達式逐一計算：1² + (-2)² + 3² + (-4)² = 1 + 4 + 9 + 16 = 30
squares_sum = sum(n * n for n in nums)
