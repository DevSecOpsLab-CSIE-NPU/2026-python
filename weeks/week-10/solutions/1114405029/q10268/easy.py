import sys

LIMIT = 63
TOO_MANY = "More than 63 trials needed."


def min_trials(ball_count, floor_count):
    """
    計算至少需要幾次試驗，才能在最壞情況下測出答案。

    ball_count：
    - 有幾顆球

    floor_count：
    - 有幾層樓

    回傳：
    - 最少試驗次數
    - 如果超過 63 次，回傳指定文字
    """

    # dp[balls] 表示：
    # 在目前 trials 次試驗內，使用 balls 顆球最多可以測幾層樓
    dp = [0] * (ball_count + 1)

    for trials in range(1, LIMIT + 1):
        # 一定要從大到小更新
        # 因為 dp[balls] 會用到上一輪的 dp[balls - 1]
        for balls in range(ball_count, 0, -1):
            dp[balls] = dp[balls] + dp[balls - 1] + 1

        # 如果目前已經可以測到 floor_count 層，就代表 trials 是答案
        if dp[ball_count] >= floor_count:
            return str(trials)

    return TOO_MANY


def main():
    outputs = []

    for line in sys.stdin:
        line = line.strip()

        # 跳過空白行
        if not line:
            continue

        ball_count, floor_count = map(int, line.split())

        # 0 0 代表輸入結束
        if ball_count == 0 and floor_count == 0:
            break

        outputs.append(min_trials(ball_count, floor_count))

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    main()