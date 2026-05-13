def solve_case(total: int, diff: int) -> str:
    if diff > total:
        return "impossible"
    if (total + diff) % 2 == 1:
        return "impossible"
    a = (total + diff) // 2
    b = (total - diff) // 2
    if a < 0 or b < 0:
        return "impossible"
    return f"{a} {b}"


def main() -> None:
    import sys

    lines = sys.stdin.read().strip().splitlines()
    if not lines:
        return
    t = int(lines[0])
    ans = []
    for i in range(1, t + 1):
        s, d = map(int, lines[i].split())
        ans.append(solve_case(s, d))
    print("\n".join(ans))


if __name__ == "__main__":
    main()
