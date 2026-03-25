"""UVA 10050 - Hartals（-easy 版本）。

這份版本以最直覺方式撰寫：
1. 從第 1 天跑到第 N 天。
2. 檢查是否為週末（Friday/Saturday），週末直接跳過。
3. 再檢查是否有任一政黨在該天發生罷工（day % h == 0）。
"""

from __future__ import annotations


def count_hartal_days_easy(days: int, hartal_params: list[int]) -> int:
    """用逐日掃描法計算罷工工作日。"""
    total = 0

    for day in range(1, days + 1):
        if day % 7 in (6, 0):
            continue

        for h in hartal_params:
            if day % h == 0:
                total += 1
                break

    return total


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

        answers.append(str(count_hartal_days_easy(days, hartal_params)))

    return "\n".join(answers)


def main() -> None:
    import sys

    print(solve_io(sys.stdin.read()))


if __name__ == "__main__":
    main()
