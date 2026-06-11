import sys
import math
def phi_gcd_sum(n):
    total = 0
    for k in range(1, n+1):
        cnt = n // k
        total += k * sum(math.gcd(i, cnt) for i in range(1, cnt+1)) 
    return total
def main():
    for line in sys.stdin:
        n = int(line.strip())
        if n == 0:
            break
        s = 0
        for i in range(1, n):
            for j in range(i+1, n+1):
                s += math.gcd(i, j)
        s += phi_gcd_sum(n)
        print(s)
