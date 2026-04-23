# 272.py
import sys

def solve():
    first = True
    for line in sys.stdin:
        res = []
        for char in line:
            if char == '"':
                if first:
                    res.append("``")
                else:
                    res.append("''")
                first = not first
            else:
                res.append(char)
        print("".join(res), end="")

if __name__ == "__main__":
    solve()
