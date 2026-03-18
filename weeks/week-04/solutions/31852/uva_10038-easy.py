"""UVA 10038: 容易記憶版本。"""

import sys


def solve(text: str) -> str:
    answers = []

    for line in text.splitlines():
        if not line.strip():
            continue

        numbers = list(map(int, line.split()))
        n = numbers[0]
        seq = numbers[1:]

        diffs = set()
        for i in range(1, n):
            # 把相鄰兩數的差值絕對值收集起來。
            diffs.add(abs(seq[i] - seq[i - 1]))

        # 如果差值集合剛好等於 1..n-1，就是 Jolly。
        if diffs == set(range(1, n)):
            answers.append("Jolly")
        else:
            answers.append("Not jolly")

    return "\n".join(answers)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))