"""UVA 10050 - Hartals（主解法）。

題意：計算因政黨罷工造成的工作日損失天數。
規則：每週的 Friday 與 Saturday 不列入罷工天數統計。
"""

from __future__ import annotations


def count_hartal_days(days: int, hartal_params: list[int]) -> int:
    """計算在指定天數內的罷工工作日總數。"""
    lost_days: set[int] = set()

    for h in hartal_params:
        day = h
        while day <= days:
            # 以 day % 7 判斷星期：
            # day % 7 == 6 -> Friday
            # day % 7 == 0 -> Saturday
            if day % 7 not in (6, 0):
                lost_days.add(day)
            day += h

    return len(lost_days)


def solve_io(data: str) -> str:
    tokens = data.split()
    if not tokens:
        return ""

    t = int(tokens[0])
    idx = 1
    answers: list[str] = []

    for _ in range(t):
        days = int(tokens[idx])
        idx += 1
        p = int(tokens[idx])
        idx += 1

        hartal_params = [int(tokens[idx + i]) for i in range(p)]
        idx += p

        answers.append(str(count_hartal_days(days, hartal_params)))

    return "\n".join(answers)


def main() -> None:
    import sys

    print(solve_io(sys.stdin.read()))


if __name__ == "__main__":
    main()
