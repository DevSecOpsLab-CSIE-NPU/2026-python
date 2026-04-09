def cycle_length(n):
    count = 1  
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count


def max_cycle(i, j):
    start, end = min(i, j), max(i, j)
    return max(cycle_length(n) for n in range(start, end + 1))


def solve():

    import sys

    for line in sys.stdin:
        i, j = map(int, line.split())
        print(i, j, max_cycle(i, j))