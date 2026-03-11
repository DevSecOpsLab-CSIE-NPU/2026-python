import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

if lines:
    max_len = max(len(line) for line in lines)
    padded = [line.ljust(max_len) for line in lines]
    n = len(padded)
    for col in range(max_len):
        row = []
        for r in range(n - 1, -1, -1):
            row.append(padded[r][col])
        print(''.join(row))
