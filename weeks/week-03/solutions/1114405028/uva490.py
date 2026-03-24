import sys


def main():
    lines = [line.rstrip("\n") for line in sys.stdin]
    if not lines:
        return

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

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
