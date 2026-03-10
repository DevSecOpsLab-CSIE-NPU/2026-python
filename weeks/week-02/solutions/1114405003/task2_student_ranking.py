from typing import List


def student_ranking(lines: List[str]) -> List[str]:
    if not lines:
        return []
    first = lines[0].strip().split()
    if len(first) < 2:
        raise ValueError("First line must contain n and k")

    n, k = int(first[0]), int(first[1])
    students = []
    for line in lines[1:1+n]:
        if not line.strip():
            continue
        name, score, age = line.strip().split()
        students.append((name, int(score), int(age)))

    sorted_students = sorted(
        students,
        key=lambda s: (-s[1], s[2], s[0])
    )
    top_k = sorted_students[:k]
    return [f"{name} {score} {age}" for name, score, age in top_k]
