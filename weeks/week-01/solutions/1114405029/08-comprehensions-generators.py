# 8 容器操作與推導式範例 (Updated)

# === 1. 列表推導式 (List Comprehension) ===
# 列表推導式是一種簡潔的方式來建立新列表
# 語法: [表達式 for 變數 in 可迭代物件 if 條件]
nums = [1, -2, 3, -4]

# 使用列表推導式過濾出正數並計算平方
# 這行程式碼的意思是:「從 nums 中取出每個數字 n, 如果 n > 0, 就將其平方後放入新列表」
positives_squared = [n * n for n in nums if n > 0]

print(positives_squared)  # Output: [1, 9]

# === 2. 字典推導式 (Dictionary Comprehension) ===
# 字典推導式可以快速建立字典
# 語法: {鍵表達式: 值表達式 for 變數 in 可迭代物件}
pairs = [('a', 1), ('b', 2)]

# 將 tuple 配對列表轉換為字典
# k 代表 key (鍵), v 代表 value (值)
lookup = {k: v for k, v in pairs}

print(lookup)  # Output: {'a': 1, 'b': 2}

# === 3. 集合推導式 (Set Comprehension) ===
# 與列表推導式類似，但會自動去除重複元素
# 語法: {表達式 for 變數 in 可迭代物件}
mixed_nums = [1, 2, 2, 3, 3, 3]
unique_squares = {n * n for n in mixed_nums}

print(unique_squares)  # Output: {1, 4, 9} (自動去重)

# === 4. 生成器表達式 (Generator Expression) ===
# 生成器表達式類似列表推導式, 但使用小括號 () 而非中括號 []
# 優點: 不會一次產生所有元素在記憶體中，而是「邊走邊算」
# 計算所有數字的平方和
squares_sum = sum(n * n for n in nums)

print(squares_sum)  # Output: 30 (1 + 4 + 9 + 16)

# [進階小技巧] 
# 如果生成器表達式是函數中唯一的參數（如 sum, max, min），外層的小括號可以省略：
# max_val = max(n for n in nums) # 正確且簡潔