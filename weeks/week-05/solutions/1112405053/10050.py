import sys


def main() -> None:
	data = sys.stdin.buffer.read().split()
	if not data:
		return

	n = int(data[0])
	idx = 1

	order = {"A": 0, "B": 1, "C": 2}
	candidates = ["A", "B", "C"]

	ballots = []
	first_count = {"A": 0, "B": 0, "C": 0}

	for _ in range(n):
		first = data[idx].decode()
		second = data[idx + 1].decode()
		idx += 3

		ballots.append((first, second))
		first_count[first] += 1

	eliminated = min(candidates, key=lambda c: (first_count[c], order[c]))

	final_count = first_count.copy()
	for first, second in ballots:
		if first == eliminated:
			final_count[first] -= 1
			final_count[second] += 1

	winner = min(candidates, key=lambda c: (-final_count[c], order[c]))
	sys.stdout.write(winner)


if __name__ == "__main__":
	main()
