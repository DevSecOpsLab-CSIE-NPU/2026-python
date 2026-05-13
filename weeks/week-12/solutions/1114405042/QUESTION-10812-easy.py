"""UVA 10812 — Beat the Spread! 的簡單記憶版解法。

這一版刻意把流程壓到最短：
1. 先算 `high = (S + D) // 2`
2. 再算 `low = S - high`
3. 只要出現不合法狀況，就輸出 `impossible`

這樣比較容易記：
先拿總和和差值去推出高分，再用總和倒回低分。
"""

from __future__ import annotations

import sys


def solve_case(total: int, diff: int) -> str:
    """把單筆測資直接轉成輸出字串。"""

    # 如果總和比差值小，低分一定會變成負數，直接無解。
    if total < diff:
        return "impossible"

    # `total + diff` 必須是偶數，才有辦法平均分成兩個整數。
    if (total + diff) % 2 != 0:
        return "impossible"

    high = (total + diff) // 2
    low = total - high

    # 再保險檢查一次，避免任何負數分數。
    if low < 0:
        return "impossible"

    return f"{high} {low}"


def main() -> None:
    """讀取輸入、逐筆計算、逐行輸出。"""

    data = sys.stdin.read().split()
    if not data:
        return

    count = int(data[0])
    answers: list[str] = []
    position = 1

    for _ in range(count):
        total = int(data[position])
        diff = int(data[position + 1])
        answers.append(solve_case(total, diff))
        position += 2

    sys.stdout.write("\n".join(answers))
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
