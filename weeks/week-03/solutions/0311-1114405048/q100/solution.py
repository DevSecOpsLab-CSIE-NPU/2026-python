import sys

memo = {}

def cycle_length(n):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n % 2 == 1:
        result = 1 + cycle_length(3 * n + 1)
    else:
        result = 1 + cycle_length(n // 2)
    memo[n] = result
    return result

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    i, j = map(int, line.split())
    start = min(i, j)
    end = max(i, j)
    max_len = 0
    for n in range(start, end + 1):
        length = cycle_length(n)
        if length > max_len:
            max_len = length
    print(i, j, max_len)
