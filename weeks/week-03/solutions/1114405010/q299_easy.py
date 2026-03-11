"""UVA 299 - Train Swapping（簡單版）"""

import sys


def count_swaps(nums):
    """用泡沫排序統計最少相鄰交換次數。"""
    arr = nums[:]
    swaps = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return swaps


def solve(data: str) -> str:
    tokens = data.split()
    if not tokens:
        return ""

    t = int(tokens[0])
    idx = 1
    out = []
    for _ in range(t):
        length = int(tokens[idx])
        idx += 1
        arr = list(map(int, tokens[idx : idx + length]))
        idx += length
        out.append(f"Optimal train swapping takes {count_swaps(arr)} swaps.")
    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
