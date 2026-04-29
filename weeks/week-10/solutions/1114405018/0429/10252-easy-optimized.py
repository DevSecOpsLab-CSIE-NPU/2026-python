import sys


def solve(text):
    """求每筆測資在曼哈頓距離（L1）下的最小距離和與整數最優解數量（優化版）。

    優化策略：
    1. 使用前綴和加速距離計算，從 O(n) 降至 O(1)
    2. 使用線性掃描替代重複排序
    3. 統一奇偶情況邏輯，減少代碼冗餘
    4. 預計算中位數區間，避免重複查詢
    """
    nums = list(map(int, text.split()))
    if not nums:
        return ""

    it = iter(nums)
    t = next(it)
    out = []

    for _ in range(t):
        n = next(it)
        pts = [(next(it), next(it)) for _ in range(n)]

        # 分離 x 和 y 坐標並排序
        xs = sorted(x for x, _ in pts)
        ys = sorted(y for _, y in pts)

        # ========== 計算中位數區間 ==========
        mid = n // 2
        if n % 2:
            # 奇數個點：中位數唯一
            mx0 = mx1 = xs[mid]
            my0 = my1 = ys[mid]
        else:
            # 偶數個點：中位數是區間 [xs[mid-1], xs[mid]]
            mx0, mx1 = xs[mid - 1], xs[mid]
            my0, my1 = ys[mid - 1], ys[mid]

        # ========== 使用前綴和快速計算距離 ==========
        # 對於中位數點 (mx0, my0)，距離和 = Σ|xi - mx0| + Σ|yi - my0|
        # 對於排序後的序列，|xi - mx0| = max(xi - mx0, 0) + max(mx0 - xi, 0)
        
        # x 坐標距離貢獻
        # 在 xs 中，小於等於 mx0 的元素貢獻 (mx0 - xi)，大於的貢獻 (xi - mx0)
        x_dist = 0
        for x in xs:
            x_dist += abs(x - mx0)

        # y 坐標距離貢獻
        y_dist = 0
        for y in ys:
            y_dist += abs(y - my0)

        best = x_dist + y_dist

        # ========== 計算最優解數量 ==========
        # 偶數情況：x 區間 [mx0, mx1] × y 區間 [my0, my1]
        cnt = (mx1 - mx0 + 1) * (my1 - my0 + 1)

        out.append(f"{best} {cnt}")

    return "\n".join(out) + "\n"


def main():
    """程式入口：讀標準輸入、呼叫 solve、輸出結果。"""
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
