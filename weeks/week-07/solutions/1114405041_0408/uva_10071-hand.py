import sys


def solve(data: str) -> str:
    answers = []

    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue

        v, t = map(int, line.split())
        answers.append(str(2 * v * t))

    return "\n".join(answers)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()