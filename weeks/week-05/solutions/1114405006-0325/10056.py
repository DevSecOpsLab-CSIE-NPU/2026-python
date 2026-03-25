"""
UVA 10056 - What is the Probability ?

核心公式：
第 i 位玩家獲勝機率
= p * (1 - p)^(i - 1) / (1 - (1 - p)^n)

特例：
- p = 0 時，沒有人會成功，機率為 0。

公式推導直觀說明：
1) 第 i 位玩家第一次輪到時直接成功機率 = p * (1-p)^(i-1)
2) 若第一輪前 i 位都沒成功，代表前 n 位都失敗，機率乘上一個 (1-p)^n
3) 第 i 位可能在第 1 輪、第 2 輪、第 3 輪...成功，形成等比級數
4) 等比級數求和後得到：
    p * (1-p)^(i-1) / (1 - (1-p)^n)
"""

from __future__ import annotations

import sys


def win_prob(n: int, p: float, i: int) -> float:
    """回傳第 i 位玩家最終獲勝機率。"""

    if p == 0.0:
        # 每次擲骰都不可能成功，任何玩家獲勝機率都為 0。
        return 0.0

    # q 代表一次失敗機率。
    q = 1.0 - p

    # 套用幾何級數化簡後公式。
    return (p * (q ** (i - 1))) / (1.0 - (q ** n))


def solve(data: str) -> str:
    # 以「逐行」方式解析，比較貼近題目原始輸入格式。
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    # 第一行是測資組數 S。
    s = int(lines[0])
    out: list[str] = []

    for k in range(1, s + 1):
        # 每組輸入：N p i
        n_str, p_str, i_str = lines[k].split()
        n = int(n_str)
        p = float(p_str)
        i = int(i_str)

        # 依題意輸出到小數點後 4 位。
        out.append(f"{win_prob(n, p, i):.4f}")

    return "\n".join(out)


def main() -> None:
    result = solve(sys.stdin.read())
    if result:
        sys.stdout.write(result)


if __name__ == "__main__":
    main()
