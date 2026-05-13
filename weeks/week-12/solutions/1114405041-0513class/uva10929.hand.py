def is_multiple_of_11(s: str) -> bool:
    total = 0
    for i, ch in enumerate(s):
        d = int(ch)
        if i % 2 == 0:
            total += d
        else:
            total -= d
    return total % 11 == 0


def main() -> None:
    import sys

    out = []
    for line in sys.stdin:
        s = line.strip()
        if s == "0":
            break
        if not s:
            continue
        if is_multiple_of_11(s):
            out.append(f"{s} is a multiple of 11.")
        else:
            out.append(f"{s} is not a multiple of 11.")
    print("\n".join(out))


if __name__ == "__main__":
    main()
