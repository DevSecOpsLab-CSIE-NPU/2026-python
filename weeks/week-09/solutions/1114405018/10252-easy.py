import sys


def solve(text):
    """求每筆測資在曼哈頓距離（L1）下的最小距離和與整數最優解數量。

    輸入（多筆）：
    - 第一個整數是測資數 t
    - 每筆先給點數 n，接著 n 組 (x, y)

    輸出（每筆一行）：
    - 最小距離和 best
    - 可達到最小值的整數點個數 cnt
    """
    # 把輸入攤平成整數序列，方便用 iterator 順序取值
    nums = list(map(int, text.split()))
    if not nums:
        return ""

    # 逐個讀取整數，避免手動管理行索引
    it = iter(nums)
    t = next(it)
    out = []

    for _ in range(t):
        # 讀入一筆測資的所有點
        n = next(it)
        pts = [(next(it), next(it)) for _ in range(n)]

        # L1 距離可分離為 x 與 y 兩個一維問題，各自取中位數即可最小化總和
        xs = sorted(x for x, _ in pts)
        ys = sorted(y for _, y in pts)

        # 奇數個點：中位數唯一，所以最優整數點只有 1 個
        if n % 2:
            mx = xs[n // 2]
            my = ys[n // 2]
            cnt = 1
        else:
            # 偶數個點：中位數是區間 [m0, m1]
            # x 與 y 各有一段可行整數區間，解數為兩區間長度相乘
            mx0, mx1 = xs[n // 2 - 1], xs[n // 2]
            my0, my1 = ys[n // 2 - 1], ys[n // 2]

            # 在中位數區間內任選一點，距離和都相同，這裡取左端點計算 best
            mx, my = mx0, my0
            cnt = (mx1 - mx0 + 1) * (my1 - my0 + 1)

        # 計算該中位數代表點的總曼哈頓距離
        best = sum(abs(x - mx) + abs(y - my) for x, y in pts)
        out.append(f"{best} {cnt}")

    # 每筆輸出一行，最後補換行符合一般 OJ 輸出習慣
    return "\n".join(out) + "\n"


def main():
    """程式入口：讀標準輸入、呼叫 solve、輸出結果。"""
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
