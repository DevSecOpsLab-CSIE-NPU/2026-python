# 8 容器操作與推導式範例

nums = [1, -2, 3, -4]
positives = [n for n in nums if n > 0]

pairs = [('a', 1), ('b', 2)]
lookup = {k: v for k, v in pairs}

squares_sum = sum(n * n for n in nums)

print(f"Positives: {positives}")
print(f"Lookup: {lookup}")
print(f"Squares Sum: {squares_sum}")
