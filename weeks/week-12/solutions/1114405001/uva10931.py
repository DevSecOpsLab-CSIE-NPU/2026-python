"""UVA 10931 - Parity"""


def solve(data: str) -> str:
    out = []
    for line in data.splitlines():
        s = line.strip()
        if not s:
            continue

        n = int(s)
        if n == 0:
            break

        b = bin(n)[2:]
        ones = b.count("1")
        out.append(f"The parity of {b} is {ones} (mod 2).")

    return "\n".join(out)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
