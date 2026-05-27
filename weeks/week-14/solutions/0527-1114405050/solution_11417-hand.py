import sys
import math

def solve():
    nums = map(int, sys.stdin.read().split())
    
    for n in nums:
        if n == 0:
            break
        total_gcd = sum(math.gcd(i, j) for i in range(1, n) for j in range(i + 1, n + 1))
        print(total_gcd)

if __name__ == '__main__':
    solve()