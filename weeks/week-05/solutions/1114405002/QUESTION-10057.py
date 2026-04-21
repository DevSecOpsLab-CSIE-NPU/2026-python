import sys


def solve(data: bytes) -> str:
    nums = list(map(int, data.split()))
    idx = 0
    out = []

    while idx < len(nums):
        n = nums[idx]
        idx += 1
        if idx + n > len(nums):
            break

        arr = nums[idx:idx + n]
        idx += n
        arr.sort()

        low = arr[(n - 1) // 2]
        high = arr[n // 2]
        count = sum(1 for x in arr if low <= x <= high)
        ways = high - low + 1

        out.append(f"{low} {count} {ways}")

    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.buffer.read()))
