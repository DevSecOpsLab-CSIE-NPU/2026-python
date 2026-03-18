def is_jolly(sequence):
    if len(sequence) <= 1:
        return True

    seen = set()
    for index in range(1, len(sequence)):
        diff = abs(sequence[index] - sequence[index - 1])
        if diff < 1 or diff >= len(sequence):
            return False
        seen.add(diff)

    return len(seen) == len(sequence) - 1


def solve(data):
    answers = []

    for line in data.splitlines():
        if not line.strip():
            continue

        numbers = list(map(int, line.split()))
        n = numbers[0]
        sequence = numbers[1 : 1 + n]

        if is_jolly(sequence):
            answers.append("Jolly")
        else:
            answers.append("Not jolly")

    return "\n".join(answers)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()), end="")