import sys

input_data = sys.stdin.read().split()
idx = 0

while idx < len(input_data):
    n = int(input_data[idx])
    idx += 1
    
    smaller_counts = [int(x) for x in input_data[idx : idx + n - 1]]
    idx += n - 1
    
    available = list(range(1, n + 1))
    result = [0] * n
    counts = [0] + smaller_counts
    
    for i in range(n - 1, -1, -1):
        rank_index = counts[i]
        result[i] = available.pop(rank_index)
        
    for cow in result:
        print(cow)