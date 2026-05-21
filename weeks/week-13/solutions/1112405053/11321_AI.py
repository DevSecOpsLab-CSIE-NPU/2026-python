import sys


def solve_case(n, m, traps):
	size = n * m
	parent = [-1] * size
	top_touch = bytearray(size)
	bottom_touch = bytearray(size)
	blocked = bytearray(size)

	def find(x):
		while parent[x] >= 0:
			if parent[parent[x]] >= 0:
				parent[x] = parent[parent[x]]
			x = parent[x]
		return x

	def union(a, b):
		a = find(a)
		b = find(b)
		if a == b:
			return a
		if parent[a] > parent[b]:
			a, b = b, a
		parent[a] += parent[b]
		parent[b] = a
		top_touch[a] |= top_touch[b]
		bottom_touch[a] |= bottom_touch[b]
		return a

	out = []
	for x, y in traps:
		idx = x * m + y
		roots = []
		combined_top = x == 0
		combined_bottom = x == n - 1

		if x > 0:
			up = idx - m
			if blocked[up]:
				r = find(up)
				if r not in roots:
					roots.append(r)
					combined_top |= bool(top_touch[r])
					combined_bottom |= bool(bottom_touch[r])
		if x + 1 < n:
			down = idx + m
			if blocked[down]:
				r = find(down)
				if r not in roots:
					roots.append(r)
					combined_top |= bool(top_touch[r])
					combined_bottom |= bool(bottom_touch[r])
		if y > 0:
			left = idx - 1
			if blocked[left]:
				r = find(left)
				if r not in roots:
					roots.append(r)
					combined_top |= bool(top_touch[r])
					combined_bottom |= bool(bottom_touch[r])
		if y + 1 < m:
			right = idx + 1
			if blocked[right]:
				r = find(right)
				if r not in roots:
					roots.append(r)
					combined_top |= bool(top_touch[r])
					combined_bottom |= bool(bottom_touch[r])

		if combined_top and combined_bottom:
			out.append('>_<')
			continue

		blocked[idx] = 1
		parent[idx] = -1
		top_touch[idx] = 1 if x == 0 else 0
		bottom_touch[idx] = 1 if x == n - 1 else 0

		root = idx
		for r in roots:
			root = union(root, r)

		out.append('<(_ _)>')

	return out


def main():
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	idx = 0
	outputs = []
	total = len(data)
	while idx + 2 < total:
		n = data[idx]
		m = data[idx + 1]
		t = data[idx + 2]
		idx += 3
		if idx + 2 * t > total:
			break
		traps = [(data[idx + i], data[idx + i + 1]) for i in range(0, 2 * t, 2)]
		idx += 2 * t
		outputs.extend(solve_case(n, m, traps))

	sys.stdout.write('\n'.join(outputs))


if __name__ == '__main__':
	main()

