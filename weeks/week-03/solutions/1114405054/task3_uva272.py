import sys

def solve():
    text = sys.stdin.read()
    output = []
    is_first = True
    for char in text:
        if char == '"':
            output.append("``" if is_first else "''")
            is_first = not is_first
        else:
            output.append(char)
    print("".join(output), end="")

if __name__ == "__main__":
    solve()