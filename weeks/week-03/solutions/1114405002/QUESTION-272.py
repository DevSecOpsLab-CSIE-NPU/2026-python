import sys


def main() -> None:
    open_quote = True
    output = []

    for line in sys.stdin:
        for char in line:
            if char == '"':
                output.append('``' if open_quote else "''")
                open_quote = not open_quote
            else:
                output.append(char)

    sys.stdout.write(''.join(output))


if __name__ == '__main__':
    main()