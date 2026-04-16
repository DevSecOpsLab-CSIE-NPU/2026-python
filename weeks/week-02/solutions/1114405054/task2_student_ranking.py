from __future__ import annotations

from dataclasses import dataclass
import sys


@dataclass(frozen=True)
class Student:
    name: str
    score: int
    age: int


def parse_input(data: str) -> tuple[list[Student], int]:
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return [], 0

    n, k = map(int, lines[0].split())
    students: list[Student] = []
    for line in lines[1 : 1 + n]:
        name, score_text, age_text = line.split()
        students.append(Student(name=name, score=int(score_text), age=int(age_text)))
    return students, k


def rank_students(students: list[Student]) -> list[Student]:
    return sorted(students, key=lambda s: (-s.score, s.age, s.name))


def solve(data: str) -> str:
    students, k = parse_input(data)
    ranked = rank_students(students)
    topk = ranked[:k]
    return "\n".join(f"{s.name} {s.score} {s.age}" for s in topk)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()