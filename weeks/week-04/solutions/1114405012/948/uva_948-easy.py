from __future__ import annotations

import re
import sys


def _is_possible(
	coin: int,
	is_heavier: bool,
	weighings: list[tuple[set[int], set[int], str]],
) -> bool:
	"""
	判斷某個假設是否成立：
	- 假設第 `coin` 顆是假的
	- 且它是偏重（is_heavier=True）或偏輕（is_heavier=False）

	只要有任何一次秤重和假設推論結果不一致，就回傳 False。
	"""
	for left, right, actual_sign in weighings:
		# delta 的意義：
		#   > 0 代表左盤較重
		#   < 0 代表左盤較輕
		#   = 0 代表兩邊平衡
		delta = 0

		# 假幣在左盤時，偏重會讓左盤變重；偏輕會讓左盤變輕
		if coin in left:
			delta += 1 if is_heavier else -1

		# 假幣在右盤時，效果方向相反
		if coin in right:
			delta += -1 if is_heavier else 1

		# 把 delta 轉成題目使用的符號
		if delta > 0:
			predicted_sign = ">"
		elif delta < 0:
			predicted_sign = "<"
		else:
			predicted_sign = "="

		if predicted_sign != actual_sign:
			return False

	return True


def solve(data: str) -> str:
	"""
	UVA 948 easy 版（好記版）

	核心做法（考場好背）：
	1. 先把輸入拆成 token（整數與 < > =）。
	2. 每組測資都「逐顆硬幣」嘗試。
	3. 每顆硬幣再分兩種假設：偏重、偏輕。
	4. 假設能解釋全部秤重，就把該硬幣列為可能答案。
	5. 最後只有唯一候選才輸出該編號，否則輸出 0。
	"""
	# 題目會有空白行，因此用 regex 解析最穩定
	tokens = re.findall(r"\d+|[<>=]", data)
	if not tokens:
		return ""

	idx = 0
	m = int(tokens[idx])
	idx += 1

	outputs: list[str] = []

	for _ in range(m):
		n = int(tokens[idx])
		k = int(tokens[idx + 1])
		idx += 2

		weighings: list[tuple[set[int], set[int], str]] = []

		for _ in range(k):
			p = int(tokens[idx])
			idx += 1

			left = {int(tokens[idx + i]) for i in range(p)}
			idx += p

			right = {int(tokens[idx + i]) for i in range(p)}
			idx += p

			sign = tokens[idx]
			idx += 1

			weighings.append((left, right, sign))

		candidates: list[int] = []

		# 逐顆硬幣檢查是否可能是假幣
		for coin in range(1, n + 1):
			if _is_possible(coin, True, weighings) or _is_possible(coin, False, weighings):
				candidates.append(coin)

		# 只有唯一候選時才可確定答案
		if len(candidates) == 1:
			outputs.append(str(candidates[0]))
		else:
			outputs.append("0")

	# 題目要求：不同測資結果之間要空一行
	return "\n\n".join(outputs)


def main() -> None:
	raw = sys.stdin.read()
	sys.stdout.write(solve(raw))


if __name__ == "__main__":
	main()

