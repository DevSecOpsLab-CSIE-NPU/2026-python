import sys


def count_swaps(arr: list[int]) -> int:
    """以最直覺的雙迴圈，計算最少相鄰交換次數（反序對數量）。"""
    swaps = 0
    n = len(arr)

    # 若 arr[i] > arr[j]（i < j），表示這兩節車廂順序顛倒，
    # 至少要透過一次相鄰交換關係才能修正。
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                swaps += 1

    return swaps


def solve(data: str) -> str:
    """讀入多組測資並輸出指定句型。"""
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

        # 保險起見：只取前 length 個數字。
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
