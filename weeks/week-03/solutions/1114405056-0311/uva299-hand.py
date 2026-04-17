import sys


def count_swaps(arr: list[int]) -> int:
    swaps = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                swaps += 1
    return swaps


def solve(data: str) -> str:
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    t = int(lines[0])
    idx = 1
    out = []

    for _ in range(t):
        length = int(lines[idx])
        idx += 1
        train = list(map(int, lines[idx].split()))
        idx += 1
        train = train[:length]
        s = count_swaps(train)
        out.append(f"Optimal train swapping takes {s} swaps.")

    return "\n".join(out)


def main() -> None:
    text = sys.stdin.read()
    ans = solve(text)
    if ans:
        print(ans)


if __name__ == "__main__":
    main()
