import sys

# Memoization dictionary to store cycle lengths
memo = {}

def cycle_length(n):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n % 2 == 0:
        length = 1 + cycle_length(n // 2)
    else:
        length = 1 + cycle_length(3 * n + 1)
    memo[n] = length
    return length

def max_cycle_length(i, j):
    max_len = 0
    for num in range(min(i, j), max(i, j) + 1):
        max_len = max(max_len, cycle_length(num))
    return max_len

def main():
    for line in sys.stdin:
        i, j = map(int, line.split())
        max_len = max_cycle_length(i, j)
        print(f"{i} {j} {max_len}")

if __name__ == "__main__":
    main()