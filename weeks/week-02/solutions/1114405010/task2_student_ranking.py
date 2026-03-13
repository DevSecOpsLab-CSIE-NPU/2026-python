"""Task 2: student ranking with multi-key sorting."""


from typing import Iterable


def rank_students(records: Iterable[tuple[str, int, int]], k: int) -> list[tuple[str, int, int]]:
    sorted_records = sorted(records, key=lambda r: (-r[1], r[2], r[0]))
    return sorted_records[: max(0, k)]


def parse_student_input(text: str) -> tuple[list[tuple[str, int, int]], int]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return [], 0

    n, k = map(int, lines[0].split())
    records: list[tuple[str, int, int]] = []
    for line in lines[1 : 1 + n]:
        name, score_text, age_text = line.split()
        records.append((name, int(score_text), int(age_text)))
    return records, k


def format_ranked(records: Iterable[tuple[str, int, int]]) -> str:
    return "\n".join(f"{name} {score} {age}" for name, score, age in records)


def main() -> None:
    import sys

    records, k = parse_student_input(sys.stdin.read())
    print(format_ranked(rank_students(records, k)))


if __name__ == "__main__":
    main()
