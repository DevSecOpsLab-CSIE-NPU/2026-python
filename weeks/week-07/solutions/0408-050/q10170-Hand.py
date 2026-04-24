import sys

def solve(s, d):
    left = s
    right = 10**8
    
    while left < right:
        mid = (left + right) // 2
        total_days = (s + mid) * (mid - s + 1) // 2
        
        if total_days >= d:
            right = mid
        else:
            left = mid + 1
            
    return left

if __name__ == '__main__':
    for line in sys.stdin:
        parts = line.split()
        if len(parts) == 2:
            s, d = map(int, parts)
            print(solve(s, d))