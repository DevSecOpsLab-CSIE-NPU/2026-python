def cycle_length(n):
    cache = {1: 1}
    def helper(x):
        if x in cache:
            return cache[x]
        if x % 2 == 0:
            cache[x] = 1 + helper(x // 2)
        else:
            cache[x] = 1 + helper(3 * x + 1)
        return cache[x]
    return helper(n)


def max_cycle_length(i, j):
    start, end = min(i, j), max(i, j)
    best = 0
    for n in range(start, end + 1):
        best = max(best, cycle_length(n))
    return best


def solve_100(input_text):
    lines = [l.strip() for l in input_text.strip().splitlines() if l.strip()]
    out = []
    for line in lines:
        a, b = map(int, line.split())
        out.append(f"{a} {b} {max_cycle_length(a, b)}")
    return "\n".join(out)

if __name__ == '__main__':
    import sys
    print(solve_100(sys.stdin.read()).strip())
