"""
UVA 10056 簡單好記版（easy）

口訣：
1) 先算失敗機率 q = 1 - p
2) 套公式：p*q^(i-1) / (1 - q^n)
3) p=0 直接是 0

詳細理解：
- 第 i 位玩家在「第一輪」獲勝機率是 p*q^(i-1)
    因為前 i-1 位都要先失敗（每次失敗機率 q），接著第 i 位成功（機率 p）。
- 若第一輪沒分出勝負，就等於所有 n 人都失敗一次，機率再乘上一個 q^n。
- 第 i 位可能在第 1 輪、第 2 輪、第 3 輪...獲勝，形成等比級數：
    p*q^(i-1) * (1 + q^n + q^(2n) + ...)
- 等比級數化簡後就是本題公式。
"""

import sys


def prob(n: int, p: float, i: int) -> float:
    """回傳第 i 位玩家最終獲勝機率。"""

    if p == 0.0:
        # 每次嘗試都不會成功，所以所有玩家獲勝機率都為 0。
        return 0.0

    # q：單次失敗機率
    q = 1.0 - p

    # 套用幾何級數公式
    return p * (q ** (i - 1)) / (1.0 - (q ** n))


def main() -> None:
    # 逐行讀取輸入，去除空白行。
    lines = [x.strip() for x in sys.stdin.read().splitlines() if x.strip()]
    if not lines:
        return

    # 第一行是測資組數 S。
    s = int(lines[0])

    # 收集每組答案，最後一次輸出。
    out = []

    for k in range(1, s + 1):
        # 每組格式：N p i
        n, p, i = lines[k].split()

        # 題目要求輸出到小數點後四位。
        out.append(f"{prob(int(n), float(p), int(i)):.4f}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
