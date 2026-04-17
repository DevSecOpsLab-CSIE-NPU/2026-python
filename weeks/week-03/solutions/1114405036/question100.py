# Collatz cycle length 100 題目解法
# 使用記憶化加速 cycle length 計算

def cycle_length(n, cache={1: 1}):
    """計算 n 的 Collatz cycle length。"""
    if n in cache:
        return cache[n]
    if n % 2 == 0:
        length = 1 + cycle_length(n // 2, cache)
    else:
        length = 1 + cycle_length(3 * n + 1, cache)
    cache[n] = length
    return length


def max_cycle_length(i, j):
    """回傳區間 [min(i,j), max(i,j)] 的最大 cycle length。"""
    start, end = min(i, j), max(i, j)
    best = 0
    for n in range(start, end + 1):
        best = max(best, cycle_length(n))
    return best


def solve_100(input_text):
    """解析輸入字串並回傳符合題目要求的輸出。"""
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    results = []
    for line in lines:
        parts = line.split()
        if len(parts) != 2:
            continue
        i, j = map(int, parts)
        results.append(f"{i} {j} {max_cycle_length(i, j)}")
    return "\n".join(results)


def main():
    import sys
    data = sys.stdin.read()
    if data.strip():
        print(solve_100(data))


if __name__ == '__main__':
    main()
