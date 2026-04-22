import sys


LIMIT = 63
TOO_MANY = "More than 63 trials needed."


def min_trials(k, n):
    # dp[eggs] 的意思是：
    # 在「目前這個試驗次數」下，
    # 如果手上有 eggs 顆球，最多可以判定多少層樓
    dp = [0] * (k + 1)

    # 從 1 次試驗開始，一直往上試到 63 次
    for trials in range(1, LIMIT + 1):
        # 轉移公式：
        # dp[m][k] = dp[m-1][k-1] + dp[m-1][k] + 1
        #
        # 用一維陣列滾動時，必須從大到小更新 eggs
        # 這樣 dp[eggs - 1] 才還會是上一輪的值
        for eggs in range(k, 0, -1):
            dp[eggs] = dp[eggs] + dp[eggs - 1] + 1

        # 如果目前已經能覆蓋至少 n 層樓
        # 代表 trials 就是最少需要的次數
        if dp[k] >= n:
            return str(trials)

    # 如果算到 63 次都還不夠，就照題目要求輸出固定句子
    return TOO_MANY


def main():
    outputs = []

    # 這題是多筆測資，一直讀到 0 0 結束
    for line in sys.stdin:
        line = line.strip()

        if not line:
            continue

        k, n = map(int, line.split())

        if k == 0 and n == 0:
            break

        outputs.append(min_trials(k, n))

    print("\n".join(outputs))


if __name__ == "__main__":
    main()