
def main() -> None:
    import sys

    text = sys.stdin.read()
    out = []
    left_quote = True

    for c in text:
        if c == '"':
            if left_quote:
                out.append("``")
            else:
                out.append("''")
            left_quote = not left_quote
        else:
            out.append(c)

    print("".join(out), end="")
if __name__ == "__main__":
    main()