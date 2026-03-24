import sys


def main():
    open_quote = True
    out = []

    for line in sys.stdin:
        converted = []
        for ch in line:
            if ch == '"':
                if open_quote:
                    converted.append("``")
                else:
                    converted.append("''")
                open_quote = not open_quote
            else:
                converted.append(ch)
        out.append("".join(converted))

    sys.stdout.write("".join(out))


if __name__ == "__main__":
    main()
