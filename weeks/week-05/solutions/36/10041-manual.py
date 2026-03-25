import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    num_test_cases = int(next(it))
    
    for _ in range(num_test_cases):
        r = int(next(it))
        addresses = sorted([int(next(it)) for _ in range(r)])
        
        median = addresses[r // 2]
        total_distance = sum(abs(addr - median) for addr in addresses)
        
        print(total_distance)

if __name__ == '__main__':
    solve()