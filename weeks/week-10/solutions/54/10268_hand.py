#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""10268. 水球測試（手打版）"""


def solve_10268() -> None:
    while True:
        eggs, floors = map(int, input().split())
        if eggs == 0:
            break

        if eggs >= 64:
            for trials in range(1, 64):
                if (1 << trials) - 1 >= floors:
                    print(trials)
                    break
            else:
                print("More than 63 trials needed.")
            continue

        dp = [0] * (eggs + 1)
        for trials in range(1, 64):
            for egg in range(eggs, 0, -1):
                dp[egg] = dp[egg] + dp[egg - 1] + 1

            if dp[eggs] >= floors:
                print(trials)
                break
        else:
            print("More than 63 trials needed.")


if __name__ == '__main__':
    solve_10268()
