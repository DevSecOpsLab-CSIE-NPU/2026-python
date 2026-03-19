def is_jolly(sequence: list[int]) -> bool:
    n = len(sequence)

    if n == 1:
        return True

    diffs = set()

    for i in range(1, n):
        diff = abs(sequence[i] - sequence[i - 1])

        if diff < 1 or diff >= n:
            return False

        diffs.add(diff)

    return len(diffs) == n - 1


def solve(data: str) -> str:
    answers = []

    for line in data.strip().splitlines():
        parts = list(map(int, line.split()))
        n = parts[0]
        sequence = parts[1:1 + n]

        if is_jolly(sequence):
            answers.append("Jolly")
        else:
            answers.append("Not jolly")

    return "\n".join(answers)


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()))