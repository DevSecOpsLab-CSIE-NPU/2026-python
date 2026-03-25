import sys


def win_probability(n: int, p: float, i: int) -> float:
    # p = 0 時永遠不會有人成功
    if p == 0.0:
        return 0.0

    # 第 i 位玩家在第一輪就獲勝的機率
    first_round = ((1.0 - p) ** (i - 1)) * p

    # 一整輪都沒人成功的機率
    cycle_fail = (1.0 - p) ** n

    # 幾何級數總和：first_round * (1 + cycle_fail + cycle_fail^2 + ...)
    return first_round / (1.0 - cycle_fail)


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    t = int(data[0])
    idx = 1
    answers = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1
        p = float(data[idx])
        idx += 1
        i = int(data[idx])
        idx += 1

        ans = win_probability(n, p, i)
        answers.append(f"{ans:.4f}")

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()
