import sys

data = [int(x) for x in sys.stdin.read().split()]

idx = 0
while idx < len(data):
    n = data[idx]
    idx += 1
    
    s_set = data[idx : idx + n]
    idx += n
    
    left_sums = {}
    
    for a in s_set:
        for b in s_set:
            for c in s_set:
                current_sum = a + b + c
                left_sums[current_sum] = left_sums.get(current_sum, 0) + 1
                
    total_solutions = 0
    
    for f in s_set:
        for d in s_set:
            for e in s_set:
                right_diff = f - d - e
                if right_diff in left_sums:
                    total_solutions += left_sums[right_diff]
                    
    print(total_solutions)