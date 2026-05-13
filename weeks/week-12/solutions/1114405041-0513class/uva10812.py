"""
UVA 10812 - Beat the Spread!

題意：給定總分 S 與分差 D，反推兩隊分數（大者在前）。
若無法得到非負整數解，輸出 impossible。
"""

from __future__ import annotations


def solve_case(total: int, diff: int) -> str:
    """回傳單筆測資答案字串。"""
    # 若分差比總分大，代表較小分會是負數，直接無解。
    if diff > total:
        return "impossible"

    # (S + D) 與 (S - D) 必須都能被 2 整除，才會是整數分數。
    if (total + diff) % 2 != 0:
        return "impossible"

    high = (total + diff) // 2
    low = (total - diff) // 2

    # 額外保險：任何負分都不合法。
    if high < 0 or low < 0:
        return "impossible"

    return f"{high} {low}"


def solve_io(data: str) -> str:
    lines = data.strip().splitlines()
    if not lines:
        return ""

    t = int(lines[0].strip())
    out = []

    for i in range(1, t + 1):
        s_str, d_str = lines[i].split()
        out.append(solve_case(int(s_str), int(d_str)))

    return "\n".join(out)


def main() -> None:
    import sys

    input_data = sys.stdin.read()
    sys.stdout.write(solve_io(input_data))


if __name__ == "__main__":
    main()
