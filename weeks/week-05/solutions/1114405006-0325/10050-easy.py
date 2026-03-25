"""
UVA 10050 簡單好記版（easy）

口訣：
1) 每個政黨從 h 開始，每次加 h
2) 週五、週六不算（day % 7 == 6 或 0）
3) 用 set 去重，最後看有幾天

詳細理解：
- 題目給你 N 天，以及每個政黨的罷會週期 h。
- 某政黨會在 h, 2h, 3h ... 天發生罷會。
- 但每週星期五、星期六是休假，不算工作天損失。
- 因為可能多個政黨同一天罷會，要用 set 避免重複計算。
"""

import sys


def main() -> None:
    # 一次讀完所有輸入並轉成整數。
    # 這樣可以用索引 i 依序取值，寫法最短也最穩定。
    nums = list(map(int, sys.stdin.read().split()))
    if not nums:
        # 若沒有輸入，直接結束。
        return

    # 第一個數字是測資組數 T。
    t = nums[0]

    # i 是目前讀到 nums 的位置。
    # 因為 nums[0] 已經是 T，所以從 1 開始。
    i = 1

    # ans 收集每組答案，最後一次輸出多行。
    ans = []

    for _ in range(t):
        # 每組先讀 N（模擬天數）
        n = nums[i]
        i += 1

        # 再讀 P（政黨數量）
        p = nums[i]
        i += 1

        # 取出這組的 P 個 hartal 參數。
        # hs 裡每個 h 代表該政黨罷會週期。
        hs = nums[i : i + p]
        i += p

        # lost 用 set，確保同一天只計算一次。
        lost = set()
        for h in hs:
            # 該政黨從第 h 天開始罷會，之後每 h 天一次。
            d = h
            while d <= n:
                # Day 1 是星期日，因此：
                # d % 7 == 6 -> 星期五
                # d % 7 == 0 -> 星期六
                # 兩天都不計入工作天損失。
                if d % 7 not in (6, 0):
                    lost.add(d)
                d += h

        # 這組答案就是損失工作天的總數。
        ans.append(str(len(lost)))

    # 按題目要求每組一行輸出。
    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    main()
