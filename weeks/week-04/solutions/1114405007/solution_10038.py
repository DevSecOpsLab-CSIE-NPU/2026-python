from __future__ import annotations


def is_jolly(sequence: list[int]) -> bool:
    length = len(sequence)
    if length <= 1:
        return True

    # 收集所有相鄰數字差值的絕對值，再與 1 到 n-1 的集合比較。
    differences = {abs(sequence[index] - sequence[index - 1]) for index in range(1, length)}
    return differences == set(range(1, length))


def solve(data: str) -> str:
    answers: list[str] = []

    for line in data.splitlines():
        if not line.strip():
            continue

        numbers = list(map(int, line.split()))
        count = numbers[0]
        sequence = numbers[1 : 1 + count]
        answers.append("Jolly" if is_jolly(sequence) else "Not jolly")

    return "\n".join(answers)


def main() -> None:
    import sys

    # 對每列序列檢查相鄰差值是否剛好形成 1 到 n-1。
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()