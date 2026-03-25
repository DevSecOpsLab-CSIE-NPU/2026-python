import sys


def main() -> None:
	# 一次讀完整份輸入（比逐行 input() 更快）
	data = sys.stdin.buffer.read().split()
	if not data:
		return

	n = int(data[0])
	idx = 1

	order = {"A": 0, "B": 1, "C": 2}
	candidates = ["A", "B", "C"]

	# ballots 只存第一、第二志願（第三志願這題不會用到）
	ballots = []
	first_count = {"A": 0, "B": 0, "C": 0}

	for _ in range(n):
		first = data[idx].decode()
		second = data[idx + 1].decode()
		idx += 3

		ballots.append((first, second))
		first_count[first] += 1

	# 找最低票候選人；同票時按 A -> B -> C
	eliminated = min(candidates, key=lambda c: (first_count[c], order[c]))

	# 棄保後重新計票：只有原本投給 eliminated 的人會改投第二志願
	final_count = first_count.copy()
	for first, second in ballots:
		if first == eliminated:
			final_count[first] -= 1
			final_count[second] += 1

	# 找最高票候選人；同票時按 A -> B -> C
	winner = min(candidates, key=lambda c: (-final_count[c], order[c]))
	sys.stdout.write(winner)


if __name__ == "__main__":
	main()
