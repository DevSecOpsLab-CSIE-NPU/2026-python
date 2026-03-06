from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Student:
    name: str
    score: int
    age: int


def rank_students(students: List[Student], k: int) -> List[Student]:
    ranked = sorted(students, key=lambda s: (-s.score, s.age, s.name))
    return ranked[: max(0, k)]


def parse_input(raw: str) -> tuple[List[Student], int]:
    lines = [line.strip() for line in raw.splitlines() if line.strip()]
    if not lines:
        return [], 0

    n, k = map(int, lines[0].split())
    students: List[Student] = []
    for line in lines[1 : 1 + n]:
        name, score, age = line.split()
        students.append(Student(name=name, score=int(score), age=int(age)))
    return students, k


def main() -> None:
    import sys

    students, k = parse_input(sys.stdin.read())
    for student in rank_students(students, k):
        print(f"{student.name} {student.score} {student.age}")


if __name__ == "__main__":
    main()
