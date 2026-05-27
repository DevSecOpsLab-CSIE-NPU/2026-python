import sys
import math

def process():
    items = sys.stdin.read().split()
    for item in items:
        n = int(item)
        if n == 0:
            break
        g = 0
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                g += math.gcd(i, j)
        print(g)

if __name__ == '__main__':
    process()
