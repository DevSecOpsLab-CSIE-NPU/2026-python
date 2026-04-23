def solve():
    import sys

    if len(sys.argv) > 1:
        input_stream = open(sys.argv[1], "r")
    else:
        input_stream = sys.stdin
    quotes = ["``", "''"]
    i = 0

    for line in input_stream:
        for char in line:
            if char == '"':
                print(quotes[i], end="")
                i = 1 - i 
            else:
                print(char, end="")


if __name__ == "__main__":
    solve()