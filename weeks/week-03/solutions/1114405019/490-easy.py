import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

max_len = max(len(l) for l in lines) if lines else 0
for i in range(len(lines)):
    lines[i] = lines[i].ljust(max_len)

for col in range(max_len):
    row = ''
    for i in range(len(lines)):
        row += lines[len(lines) - 1 - i][col]
    print(row)