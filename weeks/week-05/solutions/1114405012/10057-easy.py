import sys

nums = list(map(int, sys.stdin.read().split()))
idx = 0
out = []

while idx < len(nums):
    n = nums[idx]
    idx += 1

    arr = nums[idx:idx + n]
    idx += n
    if len(arr) < n:
        break

    arr.sort()

    if n % 2 == 1:
        a = arr[n // 2]
        count = arr.count(a)
        ways = 1
        out.append(f"{a} {count} {ways}")
    else:
        left = arr[n // 2 - 1]
        right = arr[n // 2]
        # 最小和的 A 可以是 [left, right] 的任何整數
        ways = right - left + 1

        count = 0
        for x in arr:
            if left <= x <= right:
                count += 1

        out.append(f"{left} {count} {ways}")

print("\n".join(out))
