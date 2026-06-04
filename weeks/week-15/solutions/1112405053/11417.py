import sys


def build_totients(limit: int) -> list[int]:
	phi = list(range(limit + 1))
	for i in range(2, limit + 1):
		if phi[i] == i:
			for j in range(i, limit + 1, i):
				phi[j] -= phi[j] // i
	return phi


def build_answers(limit: int) -> list[int]:
	phi = build_totients(limit)
	answers = [0] * (limit + 1)
	for n in range(2, limit + 1):
		total = 0
		for d in range(1, n + 1):
			count = n // d
			total += phi[d] * (count * (count - 1) // 2)
		answers[n] = total
	return answers


def main() -> None:
	answers = build_answers(500) 
	output = []
	for line in sys.stdin:
		n = int(line.strip())
		if n == 0:
			break
		output.append(str(answers[n]))
	sys.stdout.write("\n".join(output))


if __name__ == "__main__":
	main()
