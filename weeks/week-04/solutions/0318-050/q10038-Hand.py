import sys

for line in sys.stdin:
    parts = [int(x) for x in line.split()]
    if not parts:
        continue
        
    n = parts[0]
    seq = parts[1:]
    
    diffs = []
    for i in range(n - 1):
        diffs.append(abs(seq[i] - seq[i+1]))
        
    diffs.sort()
    
    if diffs == list(range(1, n)):
        print("Jolly")
    else:
        print("Not jolly")