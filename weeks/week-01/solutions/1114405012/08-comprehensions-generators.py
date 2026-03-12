# 8 容器操作與推導式範例

# 原始數列，裡面同時有正數與負數。
nums = [1, -2, 3, -4]

# 串列推導式（list comprehension）
# 讀法可以想成：
# 「從 nums 逐一取出 n，如果 n > 0，就把它收集進新串列。」
# 最後會得到只包含正數的新串列。
positives = [n for n in nums if n > 0]

# 這是一個由 tuple 組成的串列，每個 tuple 都像是一組 key-value。
pairs = [('a', 1), ('b', 2)]

# 字典推導式（dict comprehension）
# 讀法可以想成：
# 「從 pairs 逐一取出 k 和 v，建立成 k: v 的字典項目。」
lookup = {k: v for k, v in pairs}

# 生成器表達式（generator expression）
# 這裡不會先建立完整的平方串列，而是把每個 n * n 依序交給 sum()。
# 好處是寫法精簡，而且在大量資料時通常更省記憶體。
squares_sum = sum(n * n for n in nums)


def run_examples():
	"""執行這個檔案時，示範每一段程式的輸出結果。"""
	print('原始串列 nums =', nums)
	print('只保留正數的 positives =', positives)
	print()

	print('原始配對 pairs =', pairs)
	print('轉成字典後的 lookup =', lookup)
	print()

	print('每個數字平方後加總的結果 squares_sum =', squares_sum)


if __name__ == '__main__':
	run_examples()
