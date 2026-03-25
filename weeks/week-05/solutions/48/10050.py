import sys


def main():
    # 讀入全部 token，避免被換行格式影響
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    t = data[0]
    idx = 1
    answers = []

    for _ in range(t):
        n = data[idx]  # 模擬天數
        idx += 1
        p = data[idx]  # 政黨數
        idx += 1

        # lost[d] = True 代表第 d 天因罷會損失（1-based）
        lost = [False] * (n + 1)

        for _ in range(p):
            h = data[idx]  # 該政黨的罷會參數
            idx += 1

            # 每隔 h 天發生罷會，週五(6)與週六(0)不計
            for day in range(h, n + 1, h):
                weekday = day % 7
                if weekday == 6 or weekday == 0:
                    continue
                lost[day] = True

        answers.append(str(sum(lost)))

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()
