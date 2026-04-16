import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    arr = list(map(int, line.split()))
    n = arr[0]
    nums = arr[1:]

    if n <= 1:
        print("Jolly")
        continue
    diffs = {abs(nums[i] - nums[i - 1]) for i in range(1, n)}
    print("Jolly" if diffs == set(range(1, n)) else "Not jolly") 