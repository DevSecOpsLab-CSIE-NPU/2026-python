def ranking(students):
    """
    Sort students by:
    1. score (descending)
    2. age (ascending)
    3. name (ascending)
    """
    return sorted(students, key=lambda x: (-x["score"], x["age"], x["name"]))


def main():
    import sys

    first_line = sys.stdin.readline().strip()
    if not first_line:
        return

    n, k = map(int, first_line.split())

    students = []

    for _ in range(n):
        line = sys.stdin.readline().strip()
        name, score, age = line.split()
        students.append({
            "name": name,
            "score": int(score),
            "age": int(age)
        })

    ranked = ranking(students)

    for student in ranked[:k]:
        print(f"{student['name']} {student['score']} {student['age']}")


if __name__ == "__main__":
    main()