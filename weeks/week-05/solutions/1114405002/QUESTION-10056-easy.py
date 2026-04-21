import sys


def solve(data: bytes) -> str:
    vals = data.split()
    if not vals:
        return ""

    s = int(vals[0])
    p = 1
    ans = []

    for _ in range(s):
        n = int(vals[p])
        win_prob = float(vals[p + 1])
        target = int(vals[p + 2])
        p += 3

        # 若單次成功機率是 0，任何人都不可能獲勝。
        if win_prob == 0.0:
            ans.append("0.0000")
            continue

        # 第 target 位玩家在「第一輪就獲勝」的機率：
        # 前面 target-1 人都失敗，再由他成功。
        first_round_win = ((1.0 - win_prob) ** (target - 1)) * win_prob

        # 一整輪 n 人都失敗的機率。
        no_winner_one_round = (1.0 - win_prob) ** n

        # 總機率是無窮等比級數：
        # first_round_win * (1 + q + q^2 + ...)，其中 q = no_winner_one_round
        # => first_round_win / (1 - q)
        total = first_round_win / (1.0 - no_winner_one_round)
        ans.append(f"{total:.4f}")

    return "\n".join(ans)


if __name__ == "__main__":
    print(solve(sys.stdin.buffer.read()))
