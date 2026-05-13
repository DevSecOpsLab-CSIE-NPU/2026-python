import sys


def digit_sum_str(s: str) -> int:
    return sum(ord(ch) - ord("0") for ch in s)


def degree_of_nine(num: str) -> int | None:
    total = digit_sum_str(num)
    if total % 9 != 0:
        return None

    degree = 1
    while total != 9:
        total = digit_sum_str(str(total))
        degree += 1
    return degree


def main() -> None:
    out = []
    for line in sys.stdin:
        s = line.strip()
        if not s:
            continue
        if s == "0":
            break

        degree = degree_of_nine(s)
        if degree is None:
            out.append(f"{s} is not a multiple of 9.")
        else:
            out.append(f"{s} is a multiple of 9 and has 9-degree {degree}.")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
