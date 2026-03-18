"""UVA 10038: Jolly Jumpers。"""

import sys


def is_jolly(sequence: list[int]) -> bool:
    """確認相鄰差值是否恰好涵蓋 1 到 n-1。"""
    length = len(sequence)
    if length <= 1:
        return True

    seen = [False] * length

    for index in range(1, length):
        diff = abs(sequence[index] - sequence[index - 1])
        # 差值必須在 1 到 n-1 之間，而且不能重複出現。
        if diff <= 0 or diff >= length or seen[diff]:
            return False
        seen[diff] = True

    return True


def solve(text: str) -> str:
    outputs: list[str] = []

    for line in text.splitlines():
        parts = line.split()
        if not parts:
            continue

        count = int(parts[0])
        sequence = list(map(int, parts[1 : 1 + count]))
        outputs.append("Jolly" if is_jolly(sequence) else "Not jolly")

    return "\n".join(outputs)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))