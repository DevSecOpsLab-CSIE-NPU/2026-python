import sys


def days_until_group(s: int, k: int) -> int:
    return (s + k) * (k - s + 1) // 2


def solve_case(s: int, d: int) -> int:
    lo, hi = s, s
    while days_until_group(s, hi) < d:
        hi *= 2

    while lo < hi:
        mid = (lo + hi) // 2
        if days_until_group(s, mid) >= d:
            hi = mid
        else:
            lo = mid + 1

    return lo


def solve(data: str) -> str:
    out = []
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue
        s, d = map(int, line.split())
        out.append(str(solve_case(s, d)))
    return "\n".join(out)


def main() -> None:
    text = sys.stdin.read()
    ans = solve(text)
    if ans:
        print(ans)


if __name__ == "__main__":
    main()
