"""
UVA 10170 - The Hotel with Infinite Rooms（正式版）

題意摘要：
給定第一個旅行團人數 S，以及查詢天數 D（從第 1 天開始算），
旅館依序接待人數為 S, S+1, S+2, ... 的旅行團，
且「n 人團住 n 天」。

要求：找出第 D 天住宿的旅行團人數。

解法重點：
1. 若目前旅行團人數為 x，從 S 到 x 的總住宿天數為：
   S + (S+1) + ... + x
2. 我們要找「最小的 x」，使得這個總天數 >= D。
3. 由於總天數對 x 單調遞增，可用二分搜尋。

時間複雜度：O(log 答案)
空間複雜度：O(1)
"""

from __future__ import annotations


def days_from_s_to_x(s: int, x: int) -> int:
    """
    計算從人數 s 到 x（含）總共覆蓋幾天。

    公式：sum(s..x) = x*(x+1)/2 - (s-1)*s/2
    若 x < s，表示還沒任何團入住，回傳 0。
    """
    if x < s:
        return 0
    return x * (x + 1) // 2 - (s - 1) * s // 2


def solve_hotel(s: int, d: int) -> int:
    """
    回傳第 d 天所對應的旅行團人數。
    """
    # 先擴張右界，直到覆蓋天數已達 d。
    left = s
    right = s
    while days_from_s_to_x(s, right) < d:
        right *= 2

    # 二分找最小 x，使 days_from_s_to_x(s, x) >= d。
    while left < right:
        mid = (left + right) // 2
        if days_from_s_to_x(s, mid) >= d:
            right = mid
        else:
            left = mid + 1

    return left


def main() -> None:
    """
    讀取多行輸入，每行兩個整數 s d，輸出對應答案。
    讀到 EOF 結束。
    """
    import sys

    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        s_str, d_str = line.split()
        s = int(s_str)
        d = int(d_str)
        out.append(str(solve_hotel(s, d)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
