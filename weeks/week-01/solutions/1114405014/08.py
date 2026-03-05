# 08.py - 前導式與生成器表達式
nums = [1, -2, 3, -4]
positives = [n for n in nums if n > 0]   # 正數列表

pairs = [('a', 1), ('b', 2)]
lookup = {k: v for k, v in pairs}        # 字典推導式

squares_sum = sum(n * n for n in nums)   # 在 sum 中使用生成器表達式

print(f"nums = {nums}")
print(f"positives = {positives}")
print(f"pairs = {pairs}")
print(f"lookup = {lookup}")
print(f"squares_sum = {squares_sum}")