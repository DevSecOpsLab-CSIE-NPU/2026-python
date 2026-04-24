import sys
import math

def solve(a):
    N = a * a + 1
    for x in range(math.isqrt(N), 0, -1):
        if N % x == 0:
            y = N // x
            return 2 * a + x + y
    return -1 

if __name__ == '__main__':
    for line in sys.stdin:
        if line.strip():
            print(solve(int(line.strip())))