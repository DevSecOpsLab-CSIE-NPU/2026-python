import sys

def solve():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
            
        try:
            parts = list(map(int, line.split()))
            
            if not parts:
                continue
                
            n = parts[0]
            
            sequence = parts[1:]
            if n == 1:
                print("Jolly") 
                continue
            diffs = []
            for i in range(len(sequence) - 1):
                diff = abs(sequence[i] - sequence[i+1])
                diffs.append(diff)
            diff_set = set(diffs)
            expected_set = set(range(1, n))
            
            if diff_set == expected_set:
                print("Jolly")
            else:
                print("Not jolly")
                
        except ValueError:
            pass

if __name__ == '__main__':
    solve()