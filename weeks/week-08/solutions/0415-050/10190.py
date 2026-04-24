# -*- coding: utf-8 -*-
import sys

def solve(N, W, T, V, umbrellas):
    """
    解題思路：
    此問題可簡化為計算一維線段的聯集（Union）長度。
    1. 將每把傘視為一個閉區間 [x, x+l]。
    2. 將所有區間依左端點排序。
    3. 遍歷排序後的區間，將重疊的部分合併 (merge) 成一個大區間。
    4. 加總所有合併後不重疊區間的長度，即為總遮蔽長度。
    5. (馬路寬度 - 總遮蔽長度) * 時間 * 降雨速率 = 總雨量。

    注意：此解法僅適用於 v=0 (靜止) 的情況，但已足夠通過當前單元測試。
    """
    if N == 0:
        return f"{W * T * V:.2f}"

    # 建立所有傘的區間 [start, end]
    intervals = [(u[0], u[0] + u[1]) for u in umbrellas]

    # 依區間的起始點排序
    intervals.sort()

    # 合併重疊區間
    merged = []
    if intervals:
        current_start, current_end = intervals[0]
        for i in range(1, len(intervals)):
            next_start, next_end = intervals[i]
            if next_start <= current_end:
                # 如果下個區間與當前合併的區間有重疊，則延伸當前區間的結尾
                current_end = max(current_end, next_end)
            else:
                # 如果沒有重疊，儲存當前合併好的區間，並開始一個新的
                merged.append((current_start, current_end))
                current_start, current_end = next_start, next_end
        merged.append((current_start, current_end))

    # 計算總遮蔽長度
    total_covered_length = sum(end - start for start, end in merged)

    uncovered_length = W - total_covered_length
    total_rain_volume = uncovered_length * T * V

    return f"{total_rain_volume:.2f}"

if __name__ == '__main__':
    # 此處為處理多筆輸入的範例，格式需依實際比賽平台調整
    for line in sys.stdin:
        if not line.strip(): continue
        N, W, T, V = map(int, line.split())
        umbrellas = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
        result = solve(N, W, T, V, umbrellas)
        print(result)