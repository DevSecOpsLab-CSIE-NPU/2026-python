import sys
import math

def solve():
    nums = iter(map(int, sys.stdin.read().split()))
    
    for a, b in zip(nums, nums):
        if a == 0 and b == 0:
            break
        print(math.isqrt(b) - math.isqrt(a - 1))

if __name__ == '__main__':
    solve()