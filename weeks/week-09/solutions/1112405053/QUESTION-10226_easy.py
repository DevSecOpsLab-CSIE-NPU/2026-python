import sys


def generate_compressed_outputs(n, banned):
	"""回傳這筆測資所有合法排列的壓縮輸出。"""
	used = [False] * n
	order = []

	results = []
	previous = None

	def dfs(position):
		nonlocal previous

		if position == n:
			current = "".join(chr(ord("A") + person) for person in order)

			if previous is None:
				results.append(current)
			else:
				i = 0
				while i < n and previous[i] == current[i]:
					i += 1
				results.append(current[i:])

			previous = current
			return

		# 依 A, B, C... 嘗試，才能保證最終排列是字典序。
		for person in range(n):
			if used[person]:
				continue
			if (position + 1) in banned[person]:
				continue

			used[person] = True
			order.append(person)
			dfs(position + 1)
			order.pop()
			used[person] = False

	dfs(0)
	return results


def main():
	tokens = sys.stdin.buffer.read().split()
	if not tokens:
		return

	idx = 0
	all_case_outputs = []

	while idx < len(tokens):
		n = int(tokens[idx])
		idx += 1

		banned = []
		for _ in range(n):
			s = set()
			while True:
				pos = int(tokens[idx])
				idx += 1
				if pos == 0:
					break
				s.add(pos)
			banned.append(s)

		case_lines = generate_compressed_outputs(n, banned)
		all_case_outputs.append("\n".join(case_lines))

	sys.stdout.write("\n\n".join(all_case_outputs))


if __name__ == "__main__":
	main()
