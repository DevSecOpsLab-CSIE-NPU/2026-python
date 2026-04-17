import sys
from bisect import bisect_left, bisect_right


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
