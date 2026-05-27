import sys

def solve():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
        
    T = data[0]
    days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekdays = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    idx = 1
    for _ in range(T):
        m = data[idx]
        d = data[idx+1]
        idx += 2
        total_days = sum(days_in_month[:m]) + d
        print(weekdays[total_days % 7])

if __name__ == '__main__':
    solve()