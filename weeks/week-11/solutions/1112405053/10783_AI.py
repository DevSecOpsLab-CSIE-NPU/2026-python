def solve():
	# 讀入物品數量、載重上限與集結點座標
	n, W, g = map(int, input().split())

	items = []
	for _ in range(n):
		# 將每個貨物轉換成「距離集結點的距離」與重量
		x, w = map(int, input().split())
		items.append((abs(x - g), w))

	# 依照距離由近到遠排序，方便從近處開始分批裝載
	items.sort()

	total_cost = 0
	current_weight = 0
	current_max_distance = 0

	for distance, weight in items:
		# 若加入目前貨物後會超過載重，就先結算上一批
		if current_weight + weight > W:
			# 這一批的耗能 = 批次總重量 × 批次最遠距離
			total_cost += current_weight * current_max_distance
			current_weight = 0
			current_max_distance = 0

		# 將貨物加入目前這一批
		current_weight += weight
		current_max_distance = distance

	# 結算最後一批
	if current_weight > 0:
		total_cost += current_weight * current_max_distance

	# 輸出最小總耗能
	print(total_cost)


if __name__ == "__main__":
	solve()
