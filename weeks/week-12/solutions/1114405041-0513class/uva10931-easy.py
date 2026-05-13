"""
UVA 10931 - easy 版本

以 Python 內建 bin 直接轉二進位，再數 1 的數量。
"""


def to_output(n: int) -> str:
    bits = bin(n)[2:]
    p = bits.count("1")
    return f"The parity of {bits} is {p} (mod 2)."


def main() -> None:
    import sys

    out = []
    for line in sys.stdin:
        s = line.strip()
        if not s:
            continue
        n = int(s)
        if n == 0:
            break
        out.append(to_output(n))

    print("\n".join(out))


if __name__ == "__main__":
    main()
