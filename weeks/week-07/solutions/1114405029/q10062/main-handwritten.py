import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    n = int(input_data[0])
    smaller_counts = [int(x) for x in input_data[1:]]
    
    numbers = list(range(1, n + 1))
    result = [0] * n
    
    for i in range(n - 1, 0, -1):
        k = smaller_counts[i-1]
        result[i] = numbers.pop(k)
        
    result[0] = numbers[0]
    
    for val in result:
        print(val)

if __name__ == "__main__":
    solve()