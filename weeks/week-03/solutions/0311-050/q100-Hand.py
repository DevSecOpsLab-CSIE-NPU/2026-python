import sys

cache = {1: 1}

def get_cycle_length(n):
    orig = n
    step = 0
    
    while n not in cache:
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2
        step += 1
        
    cache[orig] = step + cache[n]
    
    return cache[orig]

def solve(i, j):
    start = min(i, j)
    end = max(i, j)
    
    max_len = 0
    for n in range(start, end + 1):
        length = get_cycle_length(n)
        if length > max_len:
            max_len = length
            
    return i, j, max_len

if __name__ == '__main__':
    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue
            
        i = int(parts[0])
        j = int(parts[1])
        
        res_i, res_j, max_len = solve(i, j)
        print(f"{res_i} {res_j} {max_len}")