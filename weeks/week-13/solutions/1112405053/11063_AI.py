import sys


def process_dataset(n, values, out_lines):
	# values: list of integers length = n*n*3
	total_Y = 0.0
	idx = 0
	for _ in range(n * n):
		R = values[idx]; G = values[idx+1]; B = values[idx+2]
		idx += 3
		X = 0.5149 * R + 0.3244 * G + 0.1607 * B
		Y = 0.2654 * R + 0.6704 * G + 0.0642 * B
		Z = 0.0248 * R + 0.1248 * G + 0.8504 * B
		total_Y += Y
		out_lines.append(f"{X:.4f} {Y:.4f} {Z:.4f}")
	avgY = total_Y / (n * n) if n > 0 else 0.0
	out_lines.append(f"The average of Y is {avgY:.4f}")


def main():
	data = sys.stdin.read().strip().split()
	if not data:
		return
	nums = list(map(int, data))
	res_lines = []
	i = 0
	L = len(nums)
	while i < L:
		n = nums[i]; i += 1
		needed = n * n * 3
		if i + needed > L:
			# not enough data; stop
			break
		vals = nums[i:i+needed]
		i += needed
		process_dataset(n, vals, res_lines)

	sys.stdout.write("\n".join(res_lines))


if __name__ == '__main__':
	main()

