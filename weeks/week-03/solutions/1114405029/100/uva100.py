import sys

def cycle_length(n):
    count = 1
    while n != 1:
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n //= 2
        count += 1
    return count

for line in sys.stdin:
    i, j = map(int, line.split())

    a = min(i, j)
    b = max(i, j)

    max_cycle = 0

    for n in range(a, b + 1):
        c = cycle_length(n)
        if c > max_cycle:
            max_cycle = c

    print(i, j, max_cycle)