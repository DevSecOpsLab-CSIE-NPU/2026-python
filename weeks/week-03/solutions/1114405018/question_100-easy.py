"""UVA 100 - easy version

題目重點：
1. 輸入每行兩個整數 i, j。
2. 需要找出區間 [min(i, j), max(i, j)] 中，最大的 cycle length。
3. 輸出格式必須保留原輸入順序：i j 最大長度。
"""

import sys
from functools import lru_cache


@lru_cache(maxsize=None)
def cycle_len(n: int) -> int:
    """回傳數字 n 的 cycle length（包含 n 本身與 1）。

    Collatz 規則：
    - n 是偶數 -> n / 2
    - n 是奇數 -> 3n + 1

    為什麼這裡用遞迴？
    - 規則本身就是「做一步，再算下一步」，很適合遞迴寫法。

    為什麼加上 @lru_cache？
    - 很多數字在不同路徑會重複出現。
    - 快取可以避免重算，讓整體速度大幅提升。
    """
    # 基底情況：n 到 1 的長度是 1（只算自己）
    if n == 1:
        return 1

    # 偶數：下一步是 n // 2，總長度 +1
    if n % 2 == 0:
        return 1 + cycle_len(n // 2)

    # 奇數：下一步是 3 * n + 1，總長度 +1
    return 1 + cycle_len(3 * n + 1)


def main() -> None:
    # 收集每一行結果，最後一次輸出，避免反覆 I/O
    out = []

    # 逐行讀標準輸入（直到 EOF）
    for line in sys.stdin:
        # 略過空白行，避免 split 出錯
        if not line.strip():
            continue

        # 讀入 i, j（保留原順序用於最後輸出）
        i, j = map(int, line.split())

        # 真正要計算的區間必須由小到大
        lo, hi = min(i, j), max(i, j)

        # 掃過整個區間，找最大 cycle length
        best = 0
        for n in range(lo, hi + 1):
            best = max(best, cycle_len(n))

        # 注意：輸出要用原本輸入的 i, j 順序
        out.append(f"{i} {j} {best}")

    # 依題目格式，每筆結果一行
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
