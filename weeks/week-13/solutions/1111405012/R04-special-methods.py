"""R04. 特殊方法（8.2–8.3）"""

from __future__ import annotations

from functools import total_ordering


@total_ordering
class Score:
    """示範比較相關的特殊方法。"""

    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def __repr__(self) -> str:
        return f"Score({self.name!r}, {self.value})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Score):
            return NotImplemented
        return self.value == other.value

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Score):
            return NotImplemented
        return self.value < other.value


class Classroom:
    """示範容器相關的特殊方法。"""

    def __init__(self, name: str):
        self.name = name
        self._students: list[str] = []

    def add(self, student: str) -> None:
        self._students.append(student)

    def __len__(self) -> int:
        return len(self._students)

    def __contains__(self, student: object) -> bool:
        return student in self._students

    def __iter__(self):
        return iter(self._students)

    def __repr__(self) -> str:
        return f"Classroom({self.name!r}, {len(self)} 人)"


def main() -> None:
    """印出課堂上示範的特殊方法效果。"""
    score_a = Score("Alice", 90)
    score_b = Score("Bob", 75)
    score_c = Score("Carol", 90)

    print(score_a > score_b)
    print(score_a == score_c)
    print(score_a != score_b)
    print(sorted([score_a, score_b, score_c]))

    classroom = Classroom("資工一甲")
    classroom.add("Alice")
    classroom.add("Bob")
    classroom.add("Carol")

    print(len(classroom))
    print("Alice" in classroom)
    print("Dave" in classroom)

    for student in classroom:
        print(student)


if __name__ == "__main__":
    main()
