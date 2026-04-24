# -*- coding: utf-8 -*-
# 這是 UVA 10190 (自動傘) 的簡易好記版 (Easy Version)
import sys

def solve(N, W, T, V, umbrellas):
    """
    簡易好記秘訣：【區間合併演算法】
    1. 把每把傘的 (位置, 長度) 轉成 [開始, 結束] 區間。
    2. 依「開始」位置排序所有區間。
    3. 建立一個 merged 串列。
    4. 遍歷排序後的區間：
       - 如果 merged 是空的，或當前區間跟 merged 最後一個不重疊 -> 直接新增。
       - 如果重疊 -> 更新 merged 最後一個區間的「結束」位置。
    5. 最後把所有合併後區間的長度加總，就是總遮蔽長度。
    """
    if N == 0:
        return f"{W * T * V:.2f}"

    # 1. 建立區間並排序 (轉成 list 以便後續修改)
    intervals = sorted([[u[0], u[0] + u[1]] for u in umbrellas])

    # 2. 合併區間 (超好記寫法)
    merged = []
    for start, end in intervals:
        # 如果 merged 是空的，或當前區間的起點 > merged 最後一個區間的終點
        if not merged or start > merged[-1][1]:
            # 沒有重疊，直接新增一個新區間
            merged.append([start, end])
        else:
            # 有重疊，更新 merged 最後一個區間的終點
            merged[-1][1] = max(merged[-1][1], end)

    # 3. 計算總遮蔽長度
    total_covered_length = sum(end - start for start, end in merged)

    # 4. 計算總雨量 (確保未遮蔽長度不為負)
    uncovered_length = max(0, W - total_covered_length)
    total_rain_volume = uncovered_length * T * V

    return f"{total_rain_volume:.2f}"

if __name__ == '__main__':
    # 萬用讀取法：把所有輸入切成一維陣列，不用再煩惱換行跟空白
    data = sys.stdin.read().split()
    idx = 0
    while idx < len(data):
        N, W, T, V = int(data[idx]), int(data[idx+1]), int(data[idx+2]), int(data[idx+3])
        idx += 4
        umbrellas = [tuple(map(int, data[idx+i*3 : idx+i*3+3])) for i in range(N)]
        idx += N * 3
        print(solve(N, W, T, V, umbrellas))