import sys


def is_symmetric(values):
    for left, right in zip(values, reversed(values)):
        if left < 0 or left != right:
            return False
    return True


def solve(data: str) -> str:
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    t = int(lines[0])
    index = 1
    answers = []

    for case in range(1, t + 1):
        n_line = lines[index]
        index += 1
        n = int(n_line.split("=")[1])

        values = []
        for _ in range(n):
            values.extend(map(int, lines[index].split()))
            index += 1

        status = "Symmetric." if is_symmetric(values) else "Non-symmetric."
        answers.append(f"Test #{case}: {status}")

    return "\n".join(answers)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
