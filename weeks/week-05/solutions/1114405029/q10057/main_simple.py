def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    results = []
    while True:
        try:
            n = int(next(it))
        except StopIteration:
            break
        nums = [int(next(it)) for _ in range(n)]
        nums.sort()
        if n % 2 == 1:
            mid = nums[n // 2]
            cnt = sum(1 for x in nums if abs(x - mid) == 0)
        else:
            mid1 = nums[n // 2 - 1]
            mid2 = nums[n // 2]
            cnt1 = sum(1 for x in nums if x == mid1)
            cnt2 = sum(1 for x in nums if x == mid2)
            if mid1 == mid2:
                cnt = cnt1 + cnt2
                mid = mid1
            else:
                cnt = cnt1
                mid = mid1
        total = sum(abs(x - mid) for x in nums)
        ways = sum(1 for x in nums if abs(x - mid) == 0)
        results.append(f"{mid} {total} {ways}")
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    solve()