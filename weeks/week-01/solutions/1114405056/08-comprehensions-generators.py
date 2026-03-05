# 8 容器操作與推導式範例

# 定義一個包含正數和負數的列表
nums = [1, -2, 3, -4]

# 使用列表推導式從nums中篩選出大於0的數，創建新列表positives
# 這是列表推導式的語法：[表達式 for 變數 in 可迭代對象 if 條件]
positives = [n for n in nums if n > 0]
print("正數列表:", positives)  # 輸出：[1, 3]

# 定義一個包含鍵值對的元組列表
pairs = [('a', 1), ('b', 2)]

# 使用字典推導式從pairs中創建字典lookup
# 這是字典推導式的語法：{鍵表達式: 值表達式 for 變數 in 可迭代對象}
lookup = {k: v for k, v in pairs}
print("字典:", lookup)  # 輸出：{'a': 1, 'b': 2}

# 使用生成器表達式計算nums中每個數的平方和
# 生成器表達式類似列表推導式，但使用圓括號，返回生成器對象，節省記憶體
# sum()函數可以接受生成器作為參數
squares_sum = sum(n * n for n in nums)
print("平方和:", squares_sum)  # 輸出：1 + 4 + 9 + 16 = 30
