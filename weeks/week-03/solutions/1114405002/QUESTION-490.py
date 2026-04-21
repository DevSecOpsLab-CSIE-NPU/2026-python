import sys


def main() -> None:
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    width = max(len(line) for line in lines)
    height = len(lines)
    rotated = []

    for column in range(width):
        row_chars = []
        for row in range(height - 1, -1, -1):
            line = lines[row]
            if column < len(line):
                row_chars.append(line[column])
            else:
                row_chars.append(" ")
        rotated.append("".join(row_chars))

    sys.stdout.write("\n".join(rotated) + ("\n" if rotated else ""))


if __name__ == "__main__":
    main()