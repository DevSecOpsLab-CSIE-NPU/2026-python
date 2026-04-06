from sys import stdin


# 第 i 位玩家第一次獲勝前，前面的人都必須失敗。
# 之後再加上前面整輪所有人都失敗的無限等比級數。
def main():
    data = stdin.read().split()
    if not data:
        return

    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx])
        p = float(data[idx + 1])
        i = int(data[idx + 2])
        idx += 3

        # 如果成功機率是 0，任何玩家都不可能獲勝。
        if p == 0:
            out.append("0.0000")
            continue

        first_win = ((1 - p) ** (i - 1)) * p
        all_fail = (1 - p) ** n
        ans = first_win / (1 - all_fail)
        out.append(f"{ans:.4f}")

    print("\n".join(out))


if __name__ == "__main__":
    main()