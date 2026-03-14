import sys


def rotate_clockwise_90(lines):
    if not lines:
        return []

    max_width = max(len(line) for line in lines)
    padded = [line.ljust(max_width) for line in lines]

    rotated = []

    for col in range(max_width):
        row = []
        for r in range(len(padded) - 1, -1, -1):
            row.append(padded[r][col])
        rotated.append("".join(row))

    return rotated


def solve(text):
    lines = text.splitlines()
    result = rotate_clockwise_90(lines)
    if not result:
        return ""
    return "\n".join(result) + "\n"


def main():
    data = sys.stdin.read()
    sys.stdout.write(solve(data))


if __name__ == "__main__":
    main()