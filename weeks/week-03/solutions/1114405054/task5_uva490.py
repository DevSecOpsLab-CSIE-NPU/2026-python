import sys

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines: return
    max_len = max(len(line) for line in lines)
    for i in range(max_len):
        for j in range(len(lines)-1, -1, -1):
            if i < len(lines[j]):
                print(lines[j][i], end="")
            else:
                print(" ", end="")
        print()

if __name__ == "__main__":
    solve()