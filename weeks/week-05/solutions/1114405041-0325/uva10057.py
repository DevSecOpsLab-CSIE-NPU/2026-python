"""UVA 10057 - A mid-summer night's dream（主解法）。

每組資料給定 n 個整數，需輸出三個值：
1. 最小可行中位數 A
2. 能讓總絕對距離最小的原陣列元素個數（落在 [low, high] 的元素數）
3. 可行中位數整數個數（high - low + 1）
"""

from __future__ import annotations


def analyze_medians(values: list[int]) -> tuple[int, int, int]:
    """回傳 (A, count_in_range, possible_count)。"""
    sorted_values = sorted(values)
    n = len(sorted_values)

    low = sorted_values[(n - 1) // 2]
    high = sorted_values[n // 2]

    count_in_range = sum(1 for v in sorted_values if low <= v <= high)
    possible_count = high - low + 1

    return low, count_in_range, possible_count


def solve_io(data: str) -> str:
    tokens = data.split()
    idx = 0
    outputs: list[str] = []

    while idx < len(tokens):
        n = int(tokens[idx])
        idx += 1

        values = [int(tokens[idx + i]) for i in range(n)]
        idx += n

        a, cnt, possible = analyze_medians(values)
        outputs.append(f"{a} {cnt} {possible}")

    return "\n".join(outputs)


def main() -> None:
    import sys

    out = solve_io(sys.stdin.read())
    if out:
        print(out)


if __name__ == "__main__":
    main()
