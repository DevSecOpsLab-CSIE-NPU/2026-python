import math
import sys

def solve(text):

    a = int(text.strip())

    target = a * a + 1
    best = 10**18

    for d in range(1, math.isqrt(target) + 1):
        if target % d == 0:
            e = target // d
            b = a + d
            c = a + e
            best = min(best, b + c)

    return str(best)

def main():
    sys.stdout.write(solve(sys.stdin.read()))

if __name__ == "__main__":
    main()
    