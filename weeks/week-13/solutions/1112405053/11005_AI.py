import sys


def main():
	# 讀入所有數字，方便一次處理一筆測資
	data = list(map(int, sys.stdin.read().split()))
	if not data:
		return
	w = data[0]
	n = data[1] if len(data) > 1 else 0
	rest = data[2:]
	if n <= 0:
		print(0)
		return
	if len(rest) < n:
		arr = rest
	else:
		arr = rest[:n]

	# 依價格排序後，用雙指標盡量湊成一組兩件
	arr.sort()
	i = 0
	j = len(arr) - 1
	groups = 0
	while i <= j:
		if i == j:
			groups += 1
			break
		if arr[i] + arr[j] <= w:
			i += 1
			j -= 1
			groups += 1
		else:
			j -= 1
			groups += 1

	# 輸出最少需要的分組數
	print(groups)


if __name__ == '__main__':
	main()

