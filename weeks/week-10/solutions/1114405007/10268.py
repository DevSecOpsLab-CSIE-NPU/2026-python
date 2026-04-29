import sys

"""
優化說明：
- 用一維滾動 DP 取代二維表格，降低記憶體使用量。
- 保留 63 次上限行為，同時讓每筆測資邏輯更精簡。
"""


LIMIT = 63


def min_trials(eggs, floors):
    reachable = [0] * (eggs + 1)

    for trials in range(1, LIMIT + 1):
        for egg_count in range(eggs, 0, -1):
            reachable[egg_count] = reachable[egg_count] + reachable[egg_count - 1] + 1
        if reachable[eggs] >= floors:
            return str(trials)

    return "More than 63 trials needed."


def solve(reader):
    answers = []

    for line in reader:
        eggs, floors = map(int, line.split())
        if eggs == 0:
            break
        answers.append(min_trials(eggs, floors))

    return "\n".join(answers)


def main():
    sys.stdout.write(solve(sys.stdin))


if __name__ == "__main__":
    main()