import sys
import math


# UVA 11417 - GCD
# 給定 N（2 <= N <= 500），計算所有 1 <= i < j <= N 的 gcd(i,j) 總和
# 本檔案為簡潔且可直接理解的完整實作（暴力法），在題目限制下可接受。
# Input: 多行，每行一個 N；以 N=0 結束
# Output: 對於每個 N 輸出一行結果（G 的值）


def solve():
    out_lines = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        if n == 0:
            break

        # 暴力計算：雙重迴圈計算 gcd
        # 對於 N 最大 500，此方法執行時間在可接受範圍
        total = 0
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                total += math.gcd(i, j)
        out_lines.append(str(total))

    sys.stdout.write('\n'.join(out_lines))


if __name__ == '__main__':
    solve()
