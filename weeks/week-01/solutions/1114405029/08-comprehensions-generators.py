# 8 容器操作與推導式範例

# 原始數字列表（同時包含正數與負數）
nums = [1, -2, 3, -4]
# 列表推導式：只保留大於 0 的元素，產生新的列表
positives = [n for n in nums if n > 0]

# 由 (鍵, 值) 組成的列表，常用來轉成字典
pairs = [('a', 1), ('b', 2)]
# 字典推導式：把每個 (k, v) 配對轉成字典項目
lookup = {k: v for k, v in pairs}

# 生成器表達式
# 逐一產生每個數字的平方，交給 sum 加總（不先建立完整列表）
squares_sum = sum(n * n for n in nums)

# ========================================
# 輸出範例：看看每個變數的實際結果
# ========================================
print("=== 列表推導式（List Comprehension） ===")
print(f"原始列表 nums: {nums}")
print(f"篩選出正數 positives: {positives}")
print("語法：[n for n in nums if n > 0]")
print()

print("=== 字典推導式（Dict Comprehension） ===")
print(f"原始配對 pairs: {pairs}")
print(f"轉成字典 lookup: {lookup}")
print("語法：{k: v for k, v in pairs}")
print()

print("=== 生成器表達式（Generator Expression） ===")
print(f"原始列表 nums: {nums}")
print(f"所有數字平方的總和: {squares_sum}")
print("語法：sum(n * n for n in nums)")
print("說明：生成器不會立刻建立完整列表，而是逐一產生值給 sum()")
print()

# 額外示範：生成器 vs 列表推導式
print("=== 進階：生成器 vs 列表的差異 ===")
# 列表推導式：立刻建立完整列表
list_squares = [n * n for n in nums]
print(f"列表推導式結果（完整列表）: {list_squares}")

# 生成器表達式：需要轉成 list 才能看內容
gen_squares = (n * n for n in nums)
print(f"生成器物件本身: {gen_squares}")
print(f"生成器轉成列表: {list(gen_squares)}")
print("重點：生成器只能用一次，第二次會是空的（已經被消耗完）")
