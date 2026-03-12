import sys

def get_cycle_length(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count

def solve():
    for line in sys.stdin:
        parts = line.split()
        if not parts: continue
        i, j = map(int, parts)
        low, high = min(i, j), max(i, j)
        max_cycle = 0
        for n in range(low, high + 1):
            max_cycle = max(max_cycle, get_cycle_length(n))
        print(f"{i} {j} {max_cycle}")

if __name__ == "__main__":
    solve()