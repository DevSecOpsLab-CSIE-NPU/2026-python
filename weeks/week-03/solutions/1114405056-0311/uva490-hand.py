import sys


def solve(data: str) -> str:
    lines = data.splitlines()
    if not lines:
        return ""

    width = max(len(line) for line in lines)
    height = len(lines)
    out = []

    for col in range(width):
        row_chars = []
        for row in range(height - 1, -1, -1):
            if col < len(lines[row]):
                row_chars.append(lines[row][col])
            else:
                row_chars.append(" ")
        out.append("".join(row_chars).rstrip())

    return "\n".join(out)


def main() -> None:
    text = sys.stdin.read()
    ans = solve(text)
    if ans:
        print(ans)


if __name__ == "__main__":
    main()
