from math import isqrt

def count_squares(n: int) -> int:
    """Return the number of perfect squares <= n."""
    if n < 0:
        return 0
    return isqrt(n)

if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        print(count_squares(n))
