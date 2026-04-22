import sys


def solve(text):
    """解題主函式。

    輸入格式（多筆測資）：
    - 每行兩個整數 k, n
    - k = 0 代表結束，不需處理

    輸出：
    - 每筆一行，最糟情況下所需的最少測試次數
    - 若超過 63 次，輸出固定句子
    """
    # 把整份輸入攤平成整數串列，方便用 iterator 逐個取值
    vals = list(map(int, text.split()))
    if not vals:
        return ""

    # 用 iterator 讓 next(it) 依序取出 k、n
    it = iter(vals)
    out = []

    while True:
        # 每回合讀一筆測資
        k = next(it)
        n = next(it)
        if k == 0:
            # k = 0 是終止符，不列入答案
            break

        # dp[e]：在「目前試驗次數 t」下，e 顆水球最多可判定的樓層數
        # 經典轉移式：dp[e] = dp[e] + dp[e-1] + 1
        # 含義：
        # - 水球破掉 -> 可向下檢查 dp[e-1] 層
        # - 水球沒破 -> 可向上檢查 dp[e] 層（上一輪的值）
        # - 加上當前這一層，共 +1
        dp = [0] * (k + 1)

        # 預設答案：若 63 次內都不夠，就輸出題目指定字串
        ans = "More than 63 trials needed."

        # 題目規定若超過 63 次就不用給數字，因此只需算到 63
        for t in range(1, 64):
            # 由大到小更新，避免 dp[e-1] 被本輪覆蓋
            for e in range(k, 0, -1):
                dp[e] = dp[e] + dp[e - 1] + 1

            # 若可覆蓋樓層已達 n，代表 t 次就足夠
            if dp[k] >= n:
                ans = str(t)
                break

        out.append(ans)

    # 依題目要求逐行輸出，每筆一行
    return "\n".join(out) + "\n"


def main():
    # 讀取標準輸入，交給 solve 後直接輸出
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
