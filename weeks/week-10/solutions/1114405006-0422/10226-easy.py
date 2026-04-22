"""UVA 10226 / ZeroJudge a219：限制排列的簡單版。

這份程式刻意把流程寫得更直觀：
先讀資料，再遞迴試每個位置，最後把排列壓縮後輸出。
"""

from __future__ import annotations

import sys


def solve(data: str) -> str:
	"""直接處理整份輸入，回傳最後答案。"""

	numbers = [int(item) for item in data.split()]
	index = 0
	all_case_outputs: list[str] = []

	while index < len(numbers):
		n = numbers[index]
		index += 1

		# 每個人各自記下「不能站的位置」，位置從 1 開始算。
		forbidden_positions = [set() for _ in range(n)]
		for person in range(n):
			while index < len(numbers):
				position = numbers[index]
				index += 1
				if position == 0:
					break
				forbidden_positions[person].add(position)

		used = [False] * n
		arrangement = [""] * n
		permutations: list[str] = []

		def dfs(position: int) -> None:
			# 位置填滿後，就得到一個合法排列。
			if position == n:
				permutations.append("".join(arrangement))
				return

			# 依照字母順序嘗試 A, B, C ...，自然就是字典序。
			for person in range(n):
				if used[person]:
					continue
				if (position + 1) in forbidden_positions[person]:
					continue

				used[person] = True
				arrangement[position] = chr(ord("A") + person)
				dfs(position + 1)
				used[person] = False

		dfs(0)

		# 題目要求只輸出和上一個排列不同的那一段。
		case_outputs: list[str] = []
		previous = ""
		for permutation in permutations:
			shared = 0
			while shared < len(previous) and shared < len(permutation):
				if previous[shared] != permutation[shared]:
					break
				shared += 1
			case_outputs.append(permutation[shared:])
			previous = permutation

		all_case_outputs.append("\n".join(case_outputs))

	return "\n\n".join(all_case_outputs)


def main() -> None:
	sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
	main()
