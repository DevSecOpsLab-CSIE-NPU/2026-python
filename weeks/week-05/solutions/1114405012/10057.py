import bisect
import sys


def solve(data: str) -> str:
    nums = list(map(int, data.split()))
    idx = 0
    outputs = []

    while idx < len(nums):
        n = nums[idx]
        idx += 1

        if idx + n > len(nums):
            break

        arr = nums[idx:idx + n]
        idx += n

        arr.sort()

        if n % 2 == 1:
            median = arr[n // 2]
            count = bisect.bisect_right(arr, median) - bisect.bisect_left(arr, median)
            outputs.append(f"{median} {count} 1")
        else:
            left_mid = arr[n // 2 - 1]
            right_mid = arr[n // 2]

            left_pos = bisect.bisect_left(arr, left_mid)
            right_pos = bisect.bisect_right(arr, right_mid)
            count = right_pos - left_pos

            possibilities = right_mid - left_mid + 1
            outputs.append(f"{left_mid} {count} {possibilities}")

    return "\n".join(outputs)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
