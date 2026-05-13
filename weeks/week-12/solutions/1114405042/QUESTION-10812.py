"""UVA 10812 — Beat the Spread! 的標準解法。

題目的核心只有一件事：
已知兩隊分數的總和 `S` 與絕對差 `D`，反推兩隊分數。

若把高分記為 `high`，低分記為 `low`，則：

`high + low = S`
`high - low = D`

把兩式相加可得 `2 * high = S + D`，
把兩式相減可得 `2 * low = S - D`。

因此只要檢查三件事就能判斷是否有解：
1. `S` 不能小於 `D`，不然低分會變成負數。
2. `S + D` 必須是偶數，不然無法平均分成兩個整數。
3. 算出來的低分必須仍然是非負整數。
"""

from __future__ import annotations

import sys
from typing import Optional, TextIO


def solve_case(total: int, diff: int) -> Optional[tuple[int, int]]:
    """根據總和與差值，回傳較大分數與較小分數。

    參數：
        total: 兩隊分數總和。
        diff:  兩隊分數的絕對差。

    回傳：
        有整數解時，回傳 `(high, low)`；若無解則回傳 `None`。
    """

    # 若總和比差值還小，代表低分會小於 0，直接判定無解。
    if total < diff:
        return None

    # 若 `total + diff` 是奇數，表示無法平均分成兩個整數。
    if (total + diff) % 2 != 0:
        return None

    high = (total + diff) // 2
    low = (total - diff) // 2

    # 題目要求分數不能是負數。
    if low < 0:
        return None

    return high, low


def parse_input(stream: TextIO) -> list[tuple[int, int]]:
    """讀取輸入資料，整理成每筆 `(S, D)` 的列表。

    這裡採用一次讀完的方式，方便測試時直接用字串模擬輸入。
    """

    tokens = stream.read().split()
    if not tokens:
        return []

    case_count = int(tokens[0])
    pairs: list[tuple[int, int]] = []
    index = 1

    # 每個測資都包含兩個整數：總和與差值。
    for _ in range(case_count):
        total = int(tokens[index])
        diff = int(tokens[index + 1])
        pairs.append((total, diff))
        index += 2

    return pairs


def main() -> None:
    """程式進入點：讀取所有測資並逐行輸出答案。"""

    cases = parse_input(sys.stdin)
    output_lines: list[str] = []

    for total, diff in cases:
        result = solve_case(total, diff)
        if result is None:
            output_lines.append("impossible")
        else:
            high, low = result
            output_lines.append(f"{high} {low}")

    sys.stdout.write("\n".join(output_lines))
    if output_lines:
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
