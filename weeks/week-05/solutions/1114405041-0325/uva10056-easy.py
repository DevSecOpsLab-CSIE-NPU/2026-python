"""UVA 10056 - What is the Probability ?（-easy 版本）。

這份版本用「循環相乘」觀念幫助記憶：
1. 先算一整輪都沒人成功的機率 cycle_fail。
2. 第 i 位玩家在第一輪成功機率 = before_i_fail * p。
3. 若前一輪都失敗，會重來同樣情況，因此形成等比級數。
"""

from __future__ import annotations


def winning_probability_easy(n: int, p: float, i: int) -> float:
    """用等比級數直覺推導版本計算機率。"""
    if p == 0.0:
        return 0.0

    q = 1.0 - p

    before_i_fail = q ** (i - 1)
    first_round_win = before_i_fail * p

    cycle_fail = q ** n

    # first_round_win * (1 + cycle_fail + cycle_fail^2 + ...)
    if cycle_fail == 1.0:
        return 0.0

    return first_round_win / (1.0 - cycle_fail)


def solve_io(data: str) -> str:
    tokens = data.split()
    if not tokens:
        return ""

    t = int(tokens[0])
    idx = 1
    outputs: list[str] = []

    for _ in range(t):
        n = int(tokens[idx])
        p = float(tokens[idx + 1])
        i = int(tokens[idx + 2])
        idx += 3

        outputs.append(f"{winning_probability_easy(n, p, i):.4f}")

    return "\n".join(outputs)


def main() -> None:
    import sys

    print(solve_io(sys.stdin.read()))


if __name__ == "__main__":
    main()
