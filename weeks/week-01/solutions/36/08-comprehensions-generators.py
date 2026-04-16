# 08-comprehensions-generators.py
# 範例：容器操作、推導式與生成器表達式

nums = [1, -2, 3, 0, 4]

# 列表推導式：過濾出正數
positive = [x for x in nums if x > 0]
print(f"正數列表: {positive}")

# 字典推導式：建立值為平方的字典
squares = {x: x * x for x in positive}
print(f"平方字典: {squares}")

# 生成器表達式：不會立即建立完整列表，適合節省記憶體
gen = (x * x for x in nums)
print(f"生成器物件: {gen}")
print(f"生成器第一個值: {next(gen)}")

# sum、min、join 範例
print(f"正數總和: {sum(positive)}")
print(f"正數最小值: {min(positive)}")
words = ['hello', 'world']
print(f"連接字串: {' '.join(words)}")

# 生成器也可以直接傳給函式使用，延遲計算
print(f"nums 平方總和: {sum(x * x for x in nums)}")
