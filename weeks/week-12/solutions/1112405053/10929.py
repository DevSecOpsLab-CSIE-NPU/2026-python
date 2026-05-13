
import sys


def main():
	data = sys.stdin.read().strip().split()
	if not data:
		return
	it = iter(map(int, data))
	out_lines = []
	try:
		while True:
			n = next(it)
			W = next(it)
			weights = [next(it) for _ in range(n)]
			bit = 1
			mask = (1 << (W + 1)) - 1
			for w in weights:
				if w > W:
					continue
				bit |= (bit << w) & mask
			achievable = bit & mask
			ans = achievable.bit_length() - 1 if achievable else 0
			out_lines.append(str(ans))
	except StopIteration:
		pass

	sys.stdout.write("\n".join(out_lines))


if __name__ == '__main__':
	main()

