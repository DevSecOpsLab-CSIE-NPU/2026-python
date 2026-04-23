import sys

for line in sys.stdin:
    nums = list(map(int, line.split()))
    n = nums[0]
    seq = nums[1:]
    if len(seq) != n:
        continue
    diffs = set()
    is_jolly = True
    for i in range(n-1):
        diff = abs(seq[i] - seq[i+1])
        if diff < 1 or diff >= n or diff in diffs:
            is_jolly = False
            break
        diffs.add(diff)
    if is_jolly and len(diffs) == n-1:
        print("Jolly")
    else:
        print("Not jolly")