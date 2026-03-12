# 9 比較、排序與 key 函式範例

# 比較運算（tuple 逐一比較）
# Python 會從左到右逐個元素比較：
# 先比第一個位置，若相同，再比第二個位置。
a = (1, 2)
b = (1, 3)
result = a < b

# 這是一個字典串列，每個字典都代表一筆資料。
rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]

# sorted(..., key=...) 表示：
# 排序前，先對每個元素套用 key 函式，
# 然後按照 key 函式回傳的值來排序。
# 這裡的 lambda r: r['uid'] 表示「拿每個字典中的 uid 當排序依據」。
rows_sorted = sorted(rows, key=lambda r: r['uid'])

# min/max 也可以搭配 key 使用，意思是：
# 不是直接比較整個字典，而是比較字典中的 uid。
smallest = min(rows, key=lambda r: r['uid'])
largest = max(rows, key=lambda r: r['uid'])


def run_examples():
	"""執行這個檔案時，示範比較與排序結果。"""
	print('tuple a =', a)
	print('tuple b =', b)
	print('a < b 的結果 =', result)
	print('原因：第一個元素都等於 1，接著比較第二個元素 2 和 3，所以結果是 True')
	print()

	print('原始 rows =', rows)
	print('依 uid 排序後的 rows_sorted =', rows_sorted)
	print('uid 最小的資料 smallest =', smallest)
	print('uid 最大的資料 largest =', largest)


if __name__ == '__main__':
	run_examples()
