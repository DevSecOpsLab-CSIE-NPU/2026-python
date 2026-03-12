"""
UVA 299 手打版（簡單好記）

最少相鄰交換次數 = 反序數。
直接雙迴圈數「前面比後面大」的組數即可。
"""


def inv_hand(arr: list[int]) -> int:
    cnt = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                cnt += 1
    return cnt


def solve_all(text: str) -> str:
    lines = [s.strip() for s in text.splitlines() if s.strip()]
    if not lines:
        return ""

    t = int(lines[0])
    p = 1
    out = []

    for _ in range(t):
        l = int(lines[p])
        p += 1

        arr = []
        if l > 0:
            arr = list(map(int, lines[p].split()))
            p += 1

        out.append(f"Optimal train swapping takes {inv_hand(arr)} swaps.")

    return "\n".join(out)


if __name__ == "__main__":
    import sys

    data = sys.stdin.read()
    if data.strip():
        print(solve_all(data))
