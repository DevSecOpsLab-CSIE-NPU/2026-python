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
            a = nums[n // 2]
            mn = sum(abs(x - a) for x in nums)
            ways = 1
        else:
            a = nums[n // 2 - 1]
            a2 = nums[n // 2]
            mn = sum(abs(x - a) for x in nums)
            mn2 = sum(abs(x - a2) for x in nums)
            if mn == mn2:
                a = a
                mn = mn
                ways = a2 - a + 1
            else:
                a = a2
                mn = mn2
                ways = 1
        results.append(f"{a} {mn} {ways}")
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    solve()