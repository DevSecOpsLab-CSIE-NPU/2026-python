import sys


def main():
	data = list(map(int, sys.stdin.read().split()))
	if not data:
		return
	w = data[0]
	if len(data) < 2:
		print(0)
		return
	n = data[1]
	arr = data[2:2 + n]
	if len(arr) < n:
		arr = data[2:]
		n = len(arr)

	arr.sort()
	i, j = 0, n - 1
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

	print(groups)


if __name__ == "__main__":
	main()

