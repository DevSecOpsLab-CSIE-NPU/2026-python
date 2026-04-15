N = 100
w = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
ans = []

for a in range(N + 1):
	for b in range(a, N + 1):
		for c in range(b, N + 1):
			if w[a][b][c]:
				continue
			ans.append(f"{a} {b} {c}")

			for k in range(1, N + 1):
				x, y, z = a + k, b + k, c + k

				if x <= N:
					t = sorted((x, b, c))
					w[t[0]][t[1]][t[2]] = 1
				if y <= N:
					t = sorted((a, y, c))
					w[t[0]][t[1]][t[2]] = 1
				if z <= N:
					t = sorted((a, b, z))
					w[t[0]][t[1]][t[2]] = 1

				if x <= N and y <= N:
					t = sorted((x, y, c))
					w[t[0]][t[1]][t[2]] = 1
				if x <= N and z <= N:
					t = sorted((x, b, z))
					w[t[0]][t[1]][t[2]] = 1
				if y <= N and z <= N:
					t = sorted((a, y, z))
					w[t[0]][t[1]][t[2]] = 1

				if z <= N:
					t = sorted((x, y, z))
					if t[2] <= N:
						w[t[0]][t[1]][t[2]] = 1

print("\n".join(ans))
