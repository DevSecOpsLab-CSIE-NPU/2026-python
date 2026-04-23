# Easy version
import sys

for line in sys.stdin:
    nums = list(map(int, line.split()))
    n = nums[0]
    seq = nums[1:]
    diffs = set(abs(seq[i] - seq[i+1]) for i in range(n-1))
    print("Jolly" if diffs == set(range(1, n)) else "Not jolly")