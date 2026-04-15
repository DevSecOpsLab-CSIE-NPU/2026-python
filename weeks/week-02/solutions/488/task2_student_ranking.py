"""Task 2: Student Ranking."""


Student = tuple[str, int, int]


def parse_header(line: str) -> tuple[int, int]:
    """Parse the first line: n k."""
    n_str, k_str = line.strip().split()
    return int(n_str), int(k_str)


def parse_student(line: str) -> Student:
    """Parse one student record: name score age."""
    name, score_str, age_str = line.strip().split()
    return name, int(score_str), int(age_str)


def rank_students(students: list[Student]) -> list[Student]:
    """Sort by score desc, age asc, name asc."""
    return sorted(students, key=lambda student: (-student[1], student[2], student[0]))


def top_k_students(students: list[Student], k: int) -> list[Student]:
    """Return top k students after sorting."""
    ranked = rank_students(students)
    return ranked[:k]


def solve(lines: list[str]) -> list[str]:
    """Solve Task 2 from input lines and return output lines."""
    if not lines:
        return []

    n, k = parse_header(lines[0])
    students = [parse_student(line) for line in lines[1:1 + n]]

    result = top_k_students(students, k)
    return [f"{name} {score} {age}" for name, score, age in result]


def main() -> None:
    import sys

    lines = [line.rstrip("\n") for line in sys.stdin]
    for output_line in solve(lines):
        print(output_line)


if __name__ == "__main__":
    main()
