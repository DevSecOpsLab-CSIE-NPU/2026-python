import sys


def solve():
    # 這題可以直接想成：
    # 每一輪都是 1 -> 2 -> 3 -> ... -> N -> 1 -> ...
    # 若這一輪第 i 位玩家成功，就由他獲勝。
    #
    # 所以第 i 位玩家獲勝的機率 =
    # 前面 i-1 位都失敗的機率 * 自己成功的機率 * 前面整輪重複的無限加總。
    # 最後會整理成一個很簡單的公式。
    lines = sys.stdin.buffer.read().splitlines()
    if not lines:
        return

    t = int(lines[0])
    answers = []

    for line in lines[1:1 + t]:
        if not line.strip():
            continue

        n_str, p_str, i_str = line.split()
        n = int(n_str)
        p = float(p_str)
        idx = int(i_str)

        fail = 1.0 - p

        # 分母是整圈都沒人成功的機率補正。
        # 也就是 1 - fail^N。
        denominator = 1.0 - (fail ** n)

        # 第 idx 位玩家要先讓前面 idx-1 位失敗，自己才有機會成功。
        probability = (fail ** (idx - 1)) * p / denominator

        answers.append(f"{probability:.4f}")

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    solve()