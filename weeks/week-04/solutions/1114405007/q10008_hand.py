def solve(data):
    lines = data.splitlines()
    if not lines:
        return ""

    total_lines = int(lines[0].strip())
    counts = {}

    for line in lines[1 : 1 + total_lines]:
        for char in line.upper():
            if "A" <= char <= "Z":
                counts[char] = counts.get(char, 0) + 1

    ordered = sorted(counts.items())
    ordered.sort(key=lambda item: item[1], reverse=True)

    answers = []
    for letter, count in ordered:
        answers.append(f"{letter} {count}")

    return "\n".join(answers)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()), end="")