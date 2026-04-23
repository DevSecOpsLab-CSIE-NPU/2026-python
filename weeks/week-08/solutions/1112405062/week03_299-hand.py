def solve():
    import sys

    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            lines = [line.strip() for line in f]
    else:
        lines = [line.strip() for line in sys.stdin]

    t = int(lines[0])
    idx = 1

    for _ in range(t):
        n = int(lines[idx])
        idx += 1
        train = list(map(int, lines[idx].split()))
        idx += 1

        # 用 enumerate 枚舉，計算每個元素後面有多少比它小的
        swaps = sum(1 for i, a in enumerate(train) for b in train[i + 1 :] if a > b)

        print(f"Optimal train swapping takes {swaps} swaps.")


if __name__ == "__main__":
    solve()