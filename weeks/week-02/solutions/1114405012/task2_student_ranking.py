import sys
from typing import List, Tuple


Student = Tuple[str, int, int]


def parse_input(raw: str) -> Tuple[List[Student], int]:
    lines = [line.strip() for line in raw.splitlines() if line.strip()]
    if not lines:
        return [], 0

    n, k = map(int, lines[0].split())
    students: List[Student] = []
    for line in lines[1 : n + 1]:
        name, score, age = line.split()
        students.append((name, int(score), int(age)))
    return students, k


def rank_students(students: List[Student]) -> List[Student]:
    return sorted(students, key=lambda item: (-item[1], item[2], item[0]))


def top_k_students(students: List[Student], k: int) -> List[Student]:
    if k <= 0:
        return []
    ranked = rank_students(students)
    return ranked[:k]


def format_students(students: List[Student]) -> str:
    return "\n".join(f"{name} {score} {age}" for name, score, age in students)


def solve(raw: str) -> str:
    students, k = parse_input(raw)
    return format_students(top_k_students(students, k))


def main() -> None:
    raw = sys.stdin.read()
    print(solve(raw))


if __name__ == "__main__":
    main()
