import sys


def days_until_group(s: int, k: int) -> int:
    """Total days covered from group size s to k (inclusive)."""
    # 等差級數：s + (s+1) + ... + k
    return (s + k) * (k - s + 1) // 2


def solve_case(s: int, d: int) -> int:
    # 找最小 k，使得從 s 累加到 k 的住宿天數 >= d。
    lo, hi = s, s
    # 先倍增上界，避免直接猜太小。
    while days_until_group(s, hi) < d:
        hi *= 2

    # 再用二分搜尋精確定位答案。
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
