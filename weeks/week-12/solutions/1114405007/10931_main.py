import sys


def parity_line(n: int) -> str:
    bits = format(n, "b")
    return f"The parity of {bits} is {bits.count('1')} (mod 2)."


def main() -> None:
    out = []
    for line in sys.stdin:
        s = line.strip()
        if not s:
            continue

        n = int(s)
        if n == 0:
            break
        out.append(parity_line(n))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
