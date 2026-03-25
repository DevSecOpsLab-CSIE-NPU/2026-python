# UVA 10057 (Keystroke)（簡單好記版）
# 口訣：
# 1) 排序後取中位數
# 2) 計算等於中位數的個數
# 3) 計算能達最小值的 A 範圍（偶數時取左右中位數差+1，奇數時為1）

import sys


def main() -> None:
    while True:
        n = int(input())
        if n == 0:
            break

        nums = list(map(int, input().split()))
        nums.sort()

        # 取中位數（奇數取中間，偶數取左中位數）
        if n % 2 == 1:
            a = nums[n // 2]
        else:
            a = nums[n // 2 - 1]

        # 有多少個數等於中位數
        cnt_eq = sum(1 for x in nums if x == a)

        # 有多少個不同的 A 能達最小值
        if n % 2 == 1:
            cnt_min = 1
        else:
            left = nums[n // 2 - 1]
            right = nums[n // 2]
            cnt_min = right - left + 1

        print(a, cnt_eq, cnt_min)


if __name__ == "__main__":
    main()
