import sys


def build_postorder(preorder: list[str], inorder: list[str]) -> list[str]:
	pos = {v: i for i, v in enumerate(inorder)}

	def dfs(pre_l: int, pre_r: int, in_l: int, in_r: int) -> list[str]:
		if pre_l > pre_r:
			return []

		root = preorder[pre_l]
		root_idx = pos[root]
		left_size = root_idx - in_l

		left_post = dfs(pre_l + 1, pre_l + left_size, in_l, root_idx - 1)
		right_post = dfs(pre_l + left_size + 1, pre_r, root_idx + 1, in_r)
		return left_post + right_post + [root]

	n = len(preorder)
	return dfs(0, n - 1, 0, n - 1)


def main() -> None:
	tokens = sys.stdin.buffer.read().split()
	if not tokens:
		return

	i = 0
	out_lines: list[str] = []

	while i < len(tokens):
		n = int(tokens[i])
		i += 1

		preorder = [tokens[i + k].decode() for k in range(n)]
		i += n
		inorder = [tokens[i + k].decode() for k in range(n)]
		i += n

		postorder = build_postorder(preorder, inorder)
		out_lines.append(" ".join(postorder)) 

	sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
	main()
