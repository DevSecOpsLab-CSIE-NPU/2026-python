def is_jolly(sequence):
    if len(sequence) <= 1:
        return True

    seen = set()

    # 計算每一對相鄰數字的差值絕對值。
    for index in range(1, len(sequence)):
        diff = abs(sequence[index] - sequence[index - 1])

        # 合法差值只能落在 1 到 n-1 之間。
        if diff < 1 or diff >= len(sequence):
            return False
        seen.add(diff)

    # 若 seen 剛好收集到所有 1 到 n-1，就表示是 Jolly Jumper。
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