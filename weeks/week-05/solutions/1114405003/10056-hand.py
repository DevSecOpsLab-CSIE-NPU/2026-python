import sys


def solve():
    # 這題直接套公式即可。
    # 第 i 位玩家獲勝機率 = 前面的人都失敗 * 自己成功 / (整輪不成功的補正)
    lines = sys.stdin.buffer.read().splitlines()
    if not lines:
        return

    t = int(lines[0])
    out = []

    for line in lines[1:1 + t]:
        if not line.strip():
            continue

        n_str, p_str, i_str = line.split()
        n = int(n_str)
        p = float(p_str)
        i = int(i_str)

        fail = 1.0 - p
        ans = (fail ** (i - 1)) * p / (1.0 - fail ** n)
        out.append(f"{ans:.4f}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()