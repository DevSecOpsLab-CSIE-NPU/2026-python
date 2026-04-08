import sys
from bisect import bisect_left, bisect_right


def main() -> None:
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	n = data[0]
	s = data[1 : 1 + n]

	left_values = []
	right_values = []

	# Left side: a * b + c
	for a in s:
		for b in s:
			ab = a * b
			for c in s:
				left_values.append(ab + c)

	# Right side: d * (e + f), with d != 0
	for d in s: 
		if d == 0:
			continue
		for e in s:
			for f in s:
				right_values.append(d * (e + f))

	right_values.sort()

	ans = 0
	for v in left_values:
		ans += bisect_right(right_values, v) - bisect_left(right_values, v)

	sys.stdout.write(str(ans))


if __name__ == "__main__":
	main()
