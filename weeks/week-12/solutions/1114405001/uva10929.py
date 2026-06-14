"""UVA 10929"""


def is_multiple_of_11(s: str) -> bool:
    diff = 0
    sign = 1
    for ch in s:
        diff += sign * int(ch)
        sign *= -1
    return diff % 11 == 0


def solve(data: str) -> str:
    out = []
    for line in data.splitlines():
        s = line.strip()
        if not s:
            continue
        if s == "0":
            break

        if is_multiple_of_11(s):
            out.append(f"{s} is a multiple of 11.")
        else:
            out.append(f"{s} is not a multiple of 11.")

    return "\n".join(out)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
