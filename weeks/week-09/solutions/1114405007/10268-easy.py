import sys


def main():
    # table[試丟次數][水球數] = 最多能確認幾層樓。
    table = [[0] * 101 for _ in range(64)]

    for trial in range(1, 64):
        for egg in range(1, 101):
            # 這次從某層丟下去：
            # 破掉 -> 往下查，少一顆水球
            # 沒破 -> 往上查，水球數不變
            table[trial][egg] = table[trial - 1][egg - 1] + table[trial - 1][egg] + 1

    ans = []
    for line in sys.stdin:
        k, n = map(int, line.split())
        if k == 0:
            break

        need = 64
        for trial in range(1, 64):
            if table[trial][k] >= n:
                need = trial
                break

        if need == 64:
            ans.append("More than 63 trials needed.")
        else:
            ans.append(str(need))

    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    main()