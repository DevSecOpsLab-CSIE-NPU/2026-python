# Hand version
n = 4
seq = [1, 4, 2, 3]
diffs = set()
for i in range(n-1):
    diff = abs(seq[i] - seq[i+1])
    diffs.add(diff)
print("Jolly" if diffs == set(range(1, n)) else "Not jolly")