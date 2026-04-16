def solve():
    import sys

    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            lines = [line.rstrip("\n") for line in f]
    else:
        lines = [line.rstrip("\n") for line in sys.stdin]

    max_len = max(len(l) for l in lines)

    for col in range(max_len):
        row_str = "".join(line[col] if col < len(line) else " " for line in lines)
        print(row_str)


if __name__ == "__main__":
    solve()