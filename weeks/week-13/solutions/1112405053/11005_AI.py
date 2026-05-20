import sys


# 解題說明：
# 每組最多兩件紀念品，且兩件價值總和不能超過 w。
# 最佳策略為先將所有價值排序，然後使用雙指標（最小與最大）進行貪婪配對：
# 若最小 + 最大 <= w，則把它們配成一組，左右指標各移動一步；否則最大單獨成一組，右指標左移一步。
# 這個方法能保證組數最少（時間複雜度 O(n log n) 來自排序，配對為 O(n)）。


def main():
	# 讀取所有輸入數字（可能跨多行），並轉為整數串列
	data = list(map(int, sys.stdin.read().split()))
	if not data:
		return

	# 第一個數是上限 w
	w = data[0]
	# 若只有 w 而沒有其他數，則沒有紀念品
	if len(data) < 2:
		print(0)
		return

	# 第二個數為紀念品數量 n，接著 n 個數為每件紀念品的價值
	n = data[1]
	arr = data[2:2 + n]
	# 若實際讀到的數量少於標示的 n（輸入可能沒有那麼多），則以實際讀到的數量為準
	if len(arr) < n:
		arr = data[2:]
		n = len(arr)

	# 對價值排序，準備使用雙指標配對
	arr.sort()
	i, j = 0, n - 1
	groups = 0
	# 雙指標從兩端向中間逼近，嘗試把最小與最大配對
	while i <= j:
		# 若只剩一個元素，則需再加一組
		if i == j:
			groups += 1
			break
		# 若最小與最大可以配成一組，兩指標都移動
		if arr[i] + arr[j] <= w:
			i += 1
			j -= 1
			groups += 1
		else:
			# 否則最大那個只能單獨成一組，右指標左移
			j -= 1
			groups += 1

	# 輸出最少需要的組數
	print(groups)


if __name__ == "__main__":
	main()

