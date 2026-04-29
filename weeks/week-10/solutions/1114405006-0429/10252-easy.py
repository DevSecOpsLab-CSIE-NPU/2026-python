"""UVA 10252：Common Permutation 的簡單版。

這份程式刻意把流程寫得更直觀：
先數每個字元出現幾次，再把兩邊共同出現的字元依序拼起來。
"""

from __future__ import annotations

import sys


def solve(data: str) -> str:
	"""直接處理整份輸入，回傳答案字串。

	優化：使用固定大小的計數陣列（256）替代 Counter，避免建立大量小物件與集合交集，
	在 ASCII 範圍字元上更快速且記憶體較低開銷。
	"""

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

		# 使用固定長度陣列（ASCII 範圍）計數，避免 Counter 的哈希開銷。
		lc = [0] * 256
		rc = [0] * 256
		# 若遇到非 ASCII 的字元，回退到 dict 計數
		fallback_left = None
		fallback_right = None
		for ch in left:
			oc = ord(ch)
			if oc < 256:
				lc[oc] += 1
			else:
				if fallback_left is None:
					fallback_left = {}
				fallback_left[ch] = fallback_left.get(ch, 0) + 1

		for ch in right:
			oc = ord(ch)
			if oc < 256:
				rc[oc] += 1
			else:
				if fallback_right is None:
					fallback_right = {}
				fallback_right[ch] = fallback_right.get(ch, 0) + 1

		parts: list[str] = []
		# 先處理 ASCII 範圍，保持字元順序
		for i in range(256):
			c = lc[i]
			if c and rc[i]:
				minc = c if c < rc[i] else rc[i]
				parts.append(chr(i) * minc)

		# 處理 fallback（若有非 ASCII 字元）—按字元排序以維持可預測順序
		if fallback_left is not None and fallback_right is not None:
			for ch in sorted(fallback_left.keys() & fallback_right.keys()):
				parts.append(ch * min(fallback_left[ch], fallback_right[ch]))

		answer_lines.append("".join(parts))

	return "\n".join(answer_lines)


def main() -> None:
	import sys
	print(solve(sys.stdin.read()), end="")


if __name__ == "__main__":
	main()