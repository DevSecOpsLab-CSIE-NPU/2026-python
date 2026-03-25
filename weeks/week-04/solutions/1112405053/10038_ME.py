import sys

for line in sys.stdin:
    parts = line.split()
    n = int(parts[0])
    if n == 1:
        print("Jolly")
        continue
    
    sequence = [int(parts[i]) for i in range(1, n + 1)]
    differences = set()
    
    for i in range(n - 1):
        diff = abs(sequence[i] - sequence[i + 1])
        differences.add(diff)
    
    if differences == set(range(1, n)):
        print("Jolly")
    else:
        print("Not jolly")
