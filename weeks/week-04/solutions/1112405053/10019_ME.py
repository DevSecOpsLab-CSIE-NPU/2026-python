import sys

for line in sys.stdin:
    tokens = line.split()
    if len(tokens) >= 2:
        print(abs(int(tokens[0]) - int(tokens[1])))
