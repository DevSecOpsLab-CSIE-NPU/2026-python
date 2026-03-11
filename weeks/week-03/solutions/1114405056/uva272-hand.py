import sys


def solve(data: str) -> str:
    close_next = False
    out = []
    for ch in data:
        if ch == '"':
            if not close_next:
                out.append("``")
            else:
                out.append("''")
            close_next = not close_next
        else:
            out.append(ch)
    return "".join(out)


def main() -> None:
    text = sys.stdin.read()
    print(solve(text), end="")


if __name__ == "__main__":
    main()
