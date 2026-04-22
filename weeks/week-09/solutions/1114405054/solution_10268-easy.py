#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
題目 10268 簡化版: 水球測試 (SIMPLIFIED)
用最簡單的遞推邏輯

核心邏輯：
1. DP[t][k] = k 個水球測試 t 次能判斷的最大樓層
2. DP[t][k] = DP[t-1][k-1] + 1 + DP[t-1][k]
3. 找到最小的 t 使得 DP[t][k] >= n
"""

def solve_10268():
    """簡化版：二分 DP"""
    while True:
        line = input().split()
        k, n = int(line[0]), int(line[1])

        if k == 0:
            break

        # DP 計算
        # dp[t][j] = 用 j 個球測試 t 次能判斷的最大樓層
        for t in range(1, 65):
            # 計算 DP[t][k]
            if k >= 64:  # 足夠多的球，用二分
                if (1 << t) - 1 >= n:
                    print(t)
                    break
            else:
                # 使用遞推
                dp = [[0] * (k + 1) for _ in range(t + 1)]

                for i in range(1, t + 1):
                    for j in range(1, k + 1):
                        if i == 1:
                            dp[i][j] = 1
                        else:
                            dp[i][j] = dp[i-1][j-1] + 1 + dp[i-1][j]

                if dp[t][k] >= n:
                    print(t)
                    break
        else:
            print("More than 63 trials needed.")


if __name__ == '__main__':
    solve_10268()
