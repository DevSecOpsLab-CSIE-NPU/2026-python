def rank_students(data, k):
    students = []
    for line in data.strip().split("\n"):
        parts = line.split()
        if len(parts) != 3:
            continue
        name, score, age = parts
        students.append((name, int(score), int(age)))

    sorted_students = sorted(
        students, key=lambda s: (-s[1], s[2], s[0])
    )
    return sorted_students[:k]

def format_output(ranked):
    return "\n".join(
        f"{name} {score} {age}" for name, score, age in ranked
    )

def main():
    import sys
    lines = sys.stdin.read().strip().split("\n")
    if not lines:
        return
    first = lines[0].split()
    if len(first) < 2:
        return
    n, k = int(first[0]), int(first[1])
    data = "\n".join(lines[1:1 + n])
    ranked = rank_students(data, k)
    sys.stdout.write(format_output(ranked) + "\n")

if __name__ == "__main__":
    main()
