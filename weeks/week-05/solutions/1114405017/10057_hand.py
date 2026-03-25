import sys
data = sys.stdin.read().split()
i = 0
while i < len(data):
    n = int(data[i])
    i += 1
    nums = sorted(map(int, data[i : i + n]))
    i += n
    m1 = nums[(n - 1) // 2]
    m2 = nums[n // 2]
    count = sum(1 for x in nums if m1 <= x <= m2)
    ans = m2 - m1 + 1
    print(f"{m1} {count} {ans}")