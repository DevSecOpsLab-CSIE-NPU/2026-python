from __future__ import annotations

import sys


def solve(data: str) -> str:
    answers = []

    for raw in data.splitlines():
        line = raw.strip()
        if not line:
            continue

        left, right = line.split()
        answers.append(str(abs(int(left) - int(right))))

    if not answers:
        return ""

    return "\n".join(answers) + "\n"


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()