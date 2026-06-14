"""UVA 10812 - Beat the Spread! (easy version)"""


def solve(data: str) -> str:
    rows = [r.strip() for r in data.splitlines() if r.strip()]
    if not rows:
        return ""

    total_cases = int(rows[0])
    answer = []

    for idx in range(1, total_cases + 1):
        s, d = map(int, rows[idx].split())

        if d > s:
            answer.append("impossible")
            continue

        bigger = (s + d) / 2
        smaller = (s - d) / 2

        if bigger.is_integer() and smaller.is_integer() and bigger >= 0 and smaller >= 0:
            answer.append(f"{int(bigger)} {int(smaller)}")
        else:
            answer.append("impossible")

    return "\n".join(answer)


def main() -> None:
    import sys

    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
