"""UVA 299 - 好記版本（-easy）。

核心想法：
1. 兩層迴圈掃過所有 pair
2. 若前面比後面大，就代表有一個反序對
3. 反序對總數就是最少相鄰交換次數
"""


def main() -> None:
    import sys

    lines = [line.strip() for line in sys.stdin if line.strip()]
    if not lines:
        return

    t = int(lines[0])
    p = 1

    for _ in range(t):
        l = int(lines[p])
        p += 1
        arr = list(map(int, lines[p].split()))
        p += 1

        swaps = 0
        # 詳細註解：
        # 對每一個位置 i，檢查它後面的每個位置 j。
        # 只要 arr[i] > arr[j]，代表 i 與 j 形成反序，
        # 在只能做「相鄰交換」的限制下，這個反序至少要花 1 次交換去修正。
        for i in range(l):
            for j in range(i + 1, l):
                if arr[i] > arr[j]:
                    swaps += 1

        print(f"Optimal train swapping takes {swaps} swaps.")


if __name__ == "__main__":
    main()
