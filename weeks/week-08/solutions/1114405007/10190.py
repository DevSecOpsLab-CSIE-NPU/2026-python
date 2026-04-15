"""UVA 10190 - 手打版本。"""

import sys


def solve(data: str) -> str:
    answers = []

    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue

        n, m = map(int, line.split())
        if n < 2 or m < 2:
            answers.append("Boring!")
            continue

        seq = [n]
        ok = True

        while n > 1:
            if n % m != 0:
                ok = False
                break
            n //= m
            seq.append(n)

        if ok and seq[-1] == 1:
            answers.append(" ".join(str(x) for x in seq))
        else:
            answers.append("Boring!")

    return "\n".join(answers)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
