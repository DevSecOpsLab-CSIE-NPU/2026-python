def solve():
	n, W, g = map(int, input().split())

	items = []
	for _ in range(n):
		x, w = map(int, input().split())
		items.append((abs(x - g), w))

	items.sort()

	total_cost = 0
	current_weight = 0
	current_max_distance = 0

	for distance, weight in items:
		if current_weight + weight > W:
			total_cost += current_weight * current_max_distance
			current_weight = 0
			current_max_distance = 0

		current_weight += weight
		current_max_distance = distance

	if current_weight > 0:
		total_cost += current_weight * current_max_distance

	print(total_cost)


if __name__ == "__main__":
	solve()
