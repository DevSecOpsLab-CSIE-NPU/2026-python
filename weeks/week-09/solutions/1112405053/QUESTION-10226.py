import sys


def solve_case(n, forbidden_positions):
	used = [False] * n
	arrangement = [0] * n
	prev = None
	out = []

	def dfs(pos):
		nonlocal prev
		if pos == n:
			cur = "".join(chr(ord("A") + idx) for idx in arrangement)
			if prev is None:
				out.append(cur)
			else:
				i = 0
				while i < n and prev[i] == cur[i]:
					i += 1
				out.append(cur[i:])
			prev = cur
			return

		# Try people in A.. order to ensure lexicographical arrangement order.
		for person in range(n):
			if used[person]:
				continue
			if (pos + 1) in forbidden_positions[person]:
				continue
			used[person] = True
			arrangement[pos] = person
			dfs(pos + 1)
			used[person] = False

	dfs(0)
	return out


def main():
	data = sys.stdin.buffer.read().split()
	if not data:
		return

	ptr = 0
	answers = []

	while ptr < len(data):
		n = int(data[ptr])
		ptr += 1

		forbidden_positions = []
		for _ in range(n):
			s = set()
			while True:
				v = int(data[ptr])
				ptr += 1
				if v == 0:
					break
				s.add(v)
			forbidden_positions.append(s)

		answers.append("\n".join(solve_case(n, forbidden_positions)))

	sys.stdout.write("\n\n".join(answers))


if __name__ == "__main__":
	main()
