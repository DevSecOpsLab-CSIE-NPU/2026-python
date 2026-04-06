from sys import stdin


# 逐天標記有沒有罷會，星期五與星期六直接跳過。
def main():
    data = stdin.read().split()
    if not data:
        return

    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1
        p = int(data[idx])
        idx += 1

        # 用布林陣列記錄每一天是否因罷會而停工。
        hartal = [False] * (n + 1)
        for _ in range(p):
            h = int(data[idx])
            idx += 1

            for day in range(h, n + 1, h):
                if day % 7 == 6 or day % 7 == 0:
                    continue
                hartal[day] = True

        out.append(str(sum(hartal)))

    print("\n".join(out))


if __name__ == "__main__":
    main()