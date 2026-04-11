import sys
for line in sys.stdin:
    parts = list(map(int, line.split()))
    if not parts: continue
    n = parts[0]
    nums = parts[1:]
    if n == 1:
        print("Jolly")
        continue
    present = [False] * n
    possible = True
    for i in range(1, n):
        diff = abs(nums[i] - nums[i-1])
        if 1 <= diff < n:
            present[diff] = True
        else:
            possible = False
            break
    if possible:
        for i in range(1, n):
            if not present[i]:
                possible = False
                break
    if possible:
        print("Jolly")
    else:
        print("Not jolly")