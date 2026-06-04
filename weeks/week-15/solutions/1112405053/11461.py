"""ZeroJudge d186 / UVA 11461 - Square Numbers

Count how many perfect squares are between a and b (inclusive) per query.
Input ends with a line "0 0".
"""
import sys
import math


def count_squares(a: int, b: int) -> int:
	if a > b:
		a, b = b, a
	lo = math.isqrt(a)
	if lo * lo < a:
		lo += 1
	hi = math.isqrt(b)
	return max(0, hi - lo + 1)


def main() -> None:
	out = []
	for line in sys.stdin:
		line = line.strip()
		if not line:
			continue
		a, b = map(int, line.split())
		if a == 0 and b == 0:
			break
		out.append(str(count_squares(a, b)))
	sys.stdout.write("\n".join(out))


if __name__ == "__main__":
	main()

