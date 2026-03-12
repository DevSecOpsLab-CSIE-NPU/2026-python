"""Task 2: Student Ranking

Given student records (name score age), sort using the rules:
 1. score desc
 2. age asc
 3. name asc

Return the top-k records as formatted lines.
"""

from __future__ import annotations

from typing import Iterable, List, Tuple


def parse_student_line(line: str) -> Tuple[str, int, int]:
    """Parse a single student record line into (name, score, age)."""
    parts = line.strip().split()
    if len(parts) != 3:
        raise ValueError(f"Expected 3 fields, got {len(parts)}: {line!r}")
    name, score_str, age_str = parts
    return name, int(score_str), int(age_str)


def rank_students(lines: Iterable[str], k: int) -> List[Tuple[str, int, int]]:
    """Rank students and return the top k records.

    Args:
        lines: Iterable of lines each containing `name score age`.
        k: Number of top students to output.

    Returns:
        A list of (name, score, age) tuples.
    """

    students = [parse_student_line(line) for line in lines if line.strip()]

    # Sorting rules: score desc, age asc, name asc
    students_sorted = sorted(
        students, key=lambda s: (-s[1], s[2], s[0])
    )

    return students_sorted[: max(0, k)]


def format_ranking(ranking: List[Tuple[str, int, int]]) -> str:
    """Format ranking results as output lines."""
    return "\n".join(f"{name} {score} {age}" for name, score, age in ranking)


def main() -> None:
    import sys

    data = sys.stdin.read().strip().splitlines()
    if not data:
        return

    header = data[0].strip().split()
    if len(header) != 2:
        raise ValueError(f"Expected header 'n k', got: {data[0]!r}")
    _, k_str = header
    k = int(k_str)

    ranking = rank_students(data[1:], k)
    if ranking:
        print(format_ranking(ranking))


if __name__ == "__main__":
    main()
