"""UVA 10922 - 2 the 9s (easy version)"""


def digit_sum(text: str) -> int:
    total = 0
    for ch in text:
        total += int(ch)
    return total


def solve(data: str) -> str:
    result = []
    for raw in data.splitlines():
        n = raw.strip()
        if not n:
            continue
        if n == "0":
            break

        s = digit_sum(n)
        if s % 9 != 0:
            result.append(f"{n} is not a multiple of 9.")
            continue

        depth = 1
        while s != 9:
            s = digit_sum(str(s))
            depth += 1

        result.append(f"{n} is a multiple of 9 and has 9-degree {depth}.")

    return "\n".join(result)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
