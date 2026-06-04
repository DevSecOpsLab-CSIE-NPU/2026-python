import math


def count_squares(a: int, b: int) -> int:
	if a > b:
		raise ValueError("a must be <= b")

	start = math.isqrt(a)
	if start * start < a:
		start += 1

	end = math.isqrt(b)
	return max(0, end - start + 1)
