"""UVA 10252：Common Permutation 的簡單版。

這份程式刻意把流程寫得更直觀：
先數每個字元出現幾次，再把兩邊共同出現的字元依序拼起來。
"""

from __future__ import annotations

from collections import Counter
import sys


def solve(data: str) -> str:
	"""直接處理整份輸入，回傳答案字串。"""

	lines = data.splitlines()
	if not lines:
		return ""

	case_count = int(lines[0].strip())
	answer_lines: list[str] = []

	index = 1
	for _ in range(case_count):
		left = lines[index].rstrip("\r")
		right = lines[index + 1].rstrip("\r")
		index += 2

		# 先把兩邊的字元次數統計出來。
		left_count = Counter(left)
		right_count = Counter(right)

		# 只保留兩邊都出現的字元，並按字元順序輸出。
		common_chars: list[str] = []
		for character in sorted(left_count.keys() & right_count.keys()):
			repeat = min(left_count[character], right_count[character])
			common_chars.append(character * repeat)

		answer_lines.append("".join(common_chars))

	return "\n".join(answer_lines)


def main() -> None:
	sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
	main()