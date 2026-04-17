def cycle_length(n, cache={1: 1}):
    if n in cache:
        return cache[n]
    if n % 2 == 0:
        result = 1 + cycle_length(n // 2, cache)
    else:
        result = 1 + cycle_length(3 * n + 1, cache)
    cache[n] = result
    return result


def max_cycle_length(i, j):
    start, end = min(i, j), max(i, j)
    return max(cycle_length(n) for n in range(start, end + 1))


def solve_100(input_text):
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    return "\n".join(f"{i} {j} {max_cycle_length(i, j)}" for i, j in (map(int, line.split()) for line in lines))

if __name__ == '__main__':
    import sys
    print(solve_100(sys.stdin.read()).strip())
