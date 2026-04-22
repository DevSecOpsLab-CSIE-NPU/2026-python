import sys

def main():
    lines = [line.rstrip('\n') for line in sys.stdin.readlines()]
    if not lines:
        return
    max_len = max(len(line) for line in lines)
    # Pad lines to max_len with spaces
    padded = [line.ljust(max_len) for line in lines]
    # Rotate 90 degrees clockwise
    # Output has max_len rows, each with len(lines) characters
    for j in range(max_len):
        row_str = ''
        for k in range(len(lines)):
            row_str += padded[len(lines) - 1 - k][j]
        print(row_str)

if __name__ == "__main__":
    main()