def parse_input(lines: list[str]) -> tuple[list[tuple[str, int, int]], int]:
	if not lines:
		return [], 0

	n, k = map(int, lines[0].split())
	students: list[tuple[str, int, int]] = []
	for row in lines[1 : 1 + n]:
		name, score_text, age_text = row.split()
		students.append((name, int(score_text), int(age_text)))
	return students, k


def rank_students(students: list[tuple[str, int, int]], k: int) -> list[tuple[str, int, int]]:
    ranked = sorted(students, key=lambda x: (-x[1], x[2], x[0]))
    return ranked[:k]


def format_output(rows: list[tuple[str, int, int]]) -> str:
    return "\n".join(f"{name} {score} {age}" for name, score, age in rows)


def main() -> None:
	first = input().strip()
	if first == "":
		print("")
		return

	n, _ = map(int, first.split())
	lines = [first]
	for _ in range(n):
		lines.append(input().strip())

	students, k = parse_input(lines)
	ranked = rank_students(students, k)
	print(format_output(ranked))


if __name__ == "__main__":
    main()
