import sys

data = [int(x) for x in sys.stdin.read().split()]

if data:
    test_cases = data[0]
    idx = 1
    
    for _ in range(test_cases):
        r = data[idx]
        idx += 1
        
        relatives = data[idx : idx + r]
        idx += r
        
        relatives.sort()
        median = relatives[r // 2]
        
        total_distance = 0
        for x in relatives:
            total_distance += abs(x - median)
            
        print(total_distance)