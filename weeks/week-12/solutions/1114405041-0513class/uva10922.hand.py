def digit_sum(s: str) -> int:
    total = 0
    for ch in s:
        total += int(ch)
    return total


def get_9_degree(s: str) -> int:
    now = digit_sum(s)
    if now % 9 != 0:
        return 0
    degree = 1
    while now != 9:
        now = digit_sum(str(now))
        degree += 1
    return degree


def main() -> None:
    import sys

    out = []
    for line in sys.stdin:
        s = line.strip()
        if s == "0":
            break
        if not s:
            continue
        degree = get_9_degree(s)
        if degree == 0:
            out.append(f"{s} is not a multiple of 9.")
        else:
            out.append(f"9-degree of {s} is {degree}.")
    print("\n".join(out))


if __name__ == "__main__":
    main()
