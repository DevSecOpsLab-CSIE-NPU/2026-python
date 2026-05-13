import sys


def is_multiple_of_11(num_str: str) -> bool:
    rem = 0
    for ch in num_str:
        rem = (rem * 10 + (ord(ch) - ord("0"))) % 11
    return rem == 0


def main() -> None:
    out = []
    for line in sys.stdin:
        s = line.strip()
        if not s:
            continue
        if s == "0":
            break

        if is_multiple_of_11(s):
            out.append(f"{s} is a multiple of 11.")
        else:
            out.append(f"{s} is not a multiple of 11.")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
