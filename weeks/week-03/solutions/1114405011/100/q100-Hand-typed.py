import sys

def cycle_length(n):
    count = 1
    while n != 1:
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2
        count += 1
    return count

def max_cycle_in_range(i, j):
    lo, hi = min(i, j), max(i, j)
    best = 0
    for n in range(lo, hi + 1):
        cl = cycle_length(n)
        if cl > best:
            best = cl
    return best

def solve(input_text):
    output_lines = []
    for line in input_text.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        i, j = map(int, line.split())
        output_lines.append(f"{i} {j} {max_cycle_in_range(i, j)}")
    return "\n".join(output_lines)

if __name__ == "__main__":
    print(solve(sys.stdin.read()))