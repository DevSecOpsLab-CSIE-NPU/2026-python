import sys

def solve(data: str) -> str:
    opened = False
    out = []
    for ch in data:
        if ch == '"':
            if not opened:
                out.append("``")
            else:
                out.append("''")
            opened = not opened
        else:
            out.append(ch)
    return "".join(out)

if __name__ == "__main__":
    print(solve(sys.stdin.read()), end="")
