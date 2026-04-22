import sys

def cycle_length(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

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