import sys


def solve_case(total: int, diff: int) -> str:
    if total < diff or (total + diff) % 2 != 0:
        return "impossible"

    a = (total + diff) // 2
    b = (total - diff) // 2
    if b < 0:
        return "impossible"
    return f"{a} {b}"


def main() -> None:
    tokens = sys.stdin.read().strip().split()
    if not tokens:
        return

    t = int(tokens[0])
    ans = []
    p = 1
    for _ in range(t):
        s = int(tokens[p])
        d = int(tokens[p + 1])
        p += 2
        ans.append(solve_case(s, d))

    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    main()
