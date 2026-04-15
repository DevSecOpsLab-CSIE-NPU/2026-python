MAX_N = 100


def mark(win, a, b, c):
	if 0 <= a <= b <= c <= MAX_N:
		win[a][b][c] = True


def main() -> None:
	# win[a][b][c] means the sorted position (a,b,c) is winning for first player.
	win = [[[False] * (MAX_N + 1) for _ in range(MAX_N + 1)] for _ in range(MAX_N + 1)]
	out = []

	for a in range(MAX_N + 1):
		for b in range(a, MAX_N + 1):
			for c in range(b, MAX_N + 1):
				if win[a][b][c]:
					continue

				# Unmarked => no move to previous losing positions => this is losing.
				out.append(f"{a} {b} {c}")

				# Mark all predecessors that can move to this losing state.
				for k in range(1, MAX_N + 1):
					x = a + k
					y = b + k
					z = c + k

					if x <= MAX_N:
						t = sorted((x, b, c))
						mark(win, t[0], t[1], t[2])
					if y <= MAX_N:
						t = sorted((a, y, c))
						mark(win, t[0], t[1], t[2])
					if z <= MAX_N:
						t = sorted((a, b, z))
						mark(win, t[0], t[1], t[2])

					if x <= MAX_N and y <= MAX_N:
						t = sorted((x, y, c))
						mark(win, t[0], t[1], t[2])
					if x <= MAX_N and z <= MAX_N:
						t = sorted((x, b, z))
						mark(win, t[0], t[1], t[2])
					if y <= MAX_N and z <= MAX_N:
						t = sorted((a, y, z))
						mark(win, t[0], t[1], t[2])

					if z <= MAX_N:
						t = sorted((x, y, z))
						if t[2] <= MAX_N:
							mark(win, t[0], t[1], t[2])

	print("\n".join(out))


if __name__ == "__main__":
	main()
