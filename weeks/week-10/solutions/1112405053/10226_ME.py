
import sys


def dfs(N, pos, used_mask, cur, forbidden, emit):
	if pos == N:
		emit(''.join(cur))
		return
	for p in range(N):
		if not (used_mask >> p) & 1:
			# person p (0..N-1) placed at position pos+1
			if (pos + 1) in forbidden[p]:
				continue
			cur.append(chr(ord('A') + p))
			dfs(N, pos + 1, used_mask | (1 << p), cur, forbidden, emit)
			cur.pop()


def solve(tokens):
	it = iter(tokens)
	out_lines = []
	first_case = True
	while True:
		try:
			N = int(next(it))
		except StopIteration:
			break
		forbidden = [set() for _ in range(N)]
		for i in range(N):
			while True:
				v = int(next(it))
				if v == 0:
					break
				forbidden[i].add(v)

		prev = ''

		def emit(s):
			nonlocal prev
			# compute common prefix length
			l = 0
			m = min(len(prev), len(s))
			while l < m and prev[l] == s[l]:
				l += 1
			out_lines.append(s[l:])
			prev = s

		dfs(N, 0, 0, [], forbidden, emit)

		# blank line between cases
		out_lines.append('')

	# remove trailing blank line if present
	if out_lines and out_lines[-1] == '':
		out_lines.pop()
	return '\n'.join(out_lines)


def main():
	data = sys.stdin.read().strip().split()
	if not data:
		return
	print(solve(data))


if __name__ == '__main__':
	main()
