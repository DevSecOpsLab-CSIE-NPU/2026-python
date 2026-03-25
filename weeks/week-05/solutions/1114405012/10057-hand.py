import bisect
import sys


def solve(data: str) -> str:
    nums = list(map(int, data.split()))
    idx = 0
    ans = []

    while idx < len(nums):
        n = nums[idx]
        idx += 1

        if idx + n > len(nums):
            break

        arr = nums[idx:idx + n]
        idx += n
        arr.sort()

        if n % 2 == 1:
            m = arr[n // 2]
            cnt = bisect.bisect_right(arr, m) - bisect.bisect_left(arr, m)
            ans.append(f"{m} {cnt} 1")
        else:
            l = arr[n // 2 - 1]
            r = arr[n // 2]
            left_idx = bisect.bisect_left(arr, l)
            right_idx = bisect.bisect_right(arr, r)
            cnt = right_idx - left_idx
            ways = r - l + 1
            ans.append(f"{l} {cnt} {ways}")

    return "\n".join(ans)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
