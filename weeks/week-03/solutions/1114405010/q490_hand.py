import sys

def solve(data: str) -> str:
    lines = data.splitlines()
    if not lines:
        return ""

    width = max(len(line) for line in lines)
    out = []

    for col in range(width):
        chars = []
        for row in range(len(lines) - 1, -1, -1):
            if col < len(lines[row]):
                chars.append(lines[row][col])
            else:
                chars.append(" ")
        out.append("".join(chars).rstrip())

    return "\n".join(out)

if __name__ == "__main__":
    print(solve(sys.stdin.read()))
