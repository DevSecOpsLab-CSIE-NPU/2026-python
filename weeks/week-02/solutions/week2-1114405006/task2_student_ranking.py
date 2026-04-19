from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List


@dataclass(frozen=True)
class Student:
    name: str
    score: int
    age: int


def parse_students(text: str) -> tuple[int, int, List[Student]]:
    tokens = text.split()
    if not tokens:
        return 0, 0, []

    n = int(tokens[0])
    k = int(tokens[1])
    students: List[Student] = []
    index = 2
    for _ in range(n):
        name = tokens[index]
        score = int(tokens[index + 1])
        age = int(tokens[index + 2])
        students.append(Student(name=name, score=score, age=age))
        index += 3
    return n, k, students


def rank_students(students: Iterable[Student]) -> List[Student]:
    return sorted(students, key=lambda student: (-student.score, student.age, student.name))


def top_k_students(students: Iterable[Student], k: int) -> List[Student]:
    ranked_students = rank_students(students)
    return ranked_students[:k]


def format_ranked_students(students: Iterable[Student]) -> str:
    return "\n".join(f"{student.name} {student.score} {student.age}" for student in students)


def solve(text: str) -> str:
    _, k, students = parse_students(text)
    return format_ranked_students(top_k_students(students, k))


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()