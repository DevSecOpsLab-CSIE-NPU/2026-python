import sys
from bisect import bisect_left, bisect_right


# UVA 10057 - A mid-summer night's dream
# 最小化 sum(|Xi - A|) 時，A 要落在中位數區間 [low, high]。
# 輸出：
# 1) low（最小可行 A）
# 2) 原數列中落在 [low, high] 的元素個數
# 3) 可行 A 的整數個數（high - low + 1）
def main() -> None:
    nums = list(map(int, sys.stdin.read().split()))
    if not nums:
        return

    idx = 0
    out = []

    while idx < len(nums):
        n = nums[idx]
        idx += 1

        arr = nums[idx:idx + n]
        idx += n
        arr.sort()

        low = arr[(n - 1) // 2]
        high = arr[n // 2]

        count = bisect_right(arr, high) - bisect_left(arr, low)
        ways = high - low + 1

        out.append(f"{low} {count} {ways}")

    print("\n".join(out))


if __name__ == "__main__":
    main()
