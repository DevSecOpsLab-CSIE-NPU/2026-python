"""UVA 100 - 簡化好記版本（-easy）。

這個版本重視「容易記憶」：
1. 函式少
2. 邏輯直觀
3. 不做太多進階技巧
"""


def cycle_len(n: int) -> int:
    """計算單一 n 的 cycle length。"""
    length = 1  # 題目定義：要把起始 n 也算進長度。

    while n != 1:
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n //= 2
        length += 1

    return length


def max_cycle(i: int, j: int) -> int:
    """找出 i 到 j（含端點）之間最大的 cycle length。"""
    if i > j:
        i, j = j, i

    best = 0
    for value in range(i, j + 1):
        best = max(best, cycle_len(value))

    return best


def main() -> None:
    """讀取多行輸入並輸出結果。"""
    import sys

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        a_str, b_str = line.split()
        a, b = int(a_str), int(b_str)
        print(f"{a} {b} {max_cycle(a, b)}")


if __name__ == "__main__":
    main()
