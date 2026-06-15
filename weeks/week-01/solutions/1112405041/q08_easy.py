# 主題 08：容器操作與推導式 - 簡易教學版

# 列表推導式（list comprehension）：用簡潔的方式建立 list
nums = [1, -2, 3, -4]
positives = [n for n in nums if n > 0]      # 只取正數 [1, 3]
print(f"正數: {positives}")

# 列表推導式可以進行轉換
doubled = [n * 2 for n in nums]             # 所有數值乘以 2 [2, -4, 6, -8]
print(f"雙倍: {doubled}")

# 字典推導式（dict comprehension）：用簡潔的方式建立 dict
pairs = [('a', 1), ('b', 2)]
lookup = {k: v for k, v in pairs}
print(f"字典: {lookup}")

# 反轉字典
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
print(f"反轉字典: {inverted}")

# 集合推導式（set comprehension）
unique_squares = {n * n for n in nums}
print(f"平方（不重複）: {unique_squares}")

# 生成器表達式（generator expression）：類似推導式，但節省記憶體
squares_gen = (n * n for n in nums)
squares_sum = sum(squares_gen)
print(f"平方和: {squares_sum}")

# 列表推導式與 if...else
result = [n if n > 0 else 0 for n in nums]  # 負數轉為 0
print(f"替換負數為 0: {result}")
