#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solve_10268():
    while True:
        line = input().split()
        k, n = int(line[0]), int(line[1])

        if k == 0:
            break

        for t in range(1, 65):
            if k >= 64:
                if (1 << t) - 1 >= n:
                    print(t)
                    break
            else:
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
