import sys

def find_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append((i, n // i))
    return factors

def main():
    a = int(sys.stdin.readline().strip())
    n = a * a + 1
    factors = find_factors(n)
    min_sum = float('inf')
    best_b = 0
    best_c = 0
    for d, e in factors:
        b = a + d
        c = a + e
        if b + c < min_sum:
            min_sum = b + c
            best_b = b
            best_c = c
        # also check swapped if d != e
        if d != e:
            b = a + e
            c = a + d
            if b + c < min_sum:
                min_sum = b + c
                best_b = b
                best_c = c
    print(best_b + best_c)

if __name__ == "__main__":
    main()