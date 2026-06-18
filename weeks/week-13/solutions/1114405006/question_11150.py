from typing import List
import heapq
from math import gcd


"""
優化版解法：計算青蛙過河時最少需踩到的石子數

註解（繁體中文）：
- 直接在整個座標上做最短路或 DP 當 L 很大時會不切實際，因此採用座標壓縮 + 最短路。
- 核心想法：只保留「重要位置」(石子位置、起點、終點) 並嘗試把兩個重要位置之間過長的空白區段縮短（shift），
  以降低狀態空間大小，但在縮短時要小心不要改變能否到達某些殘類（mod 類別）的性質。

- 特殊情況：若 S == T（固定步長），落點集合為 0, S, 2S, ...，此時最少踩石子數可直接計算。

- 壓縮規則（在本實作中採保守縮短 threshold）：
  - 若 gap 過大，則把後續座標一起左移一段距離，並相對縮短終點 L。
  - 實作中使用一個安全的 threshold（90），在 S,T 範圍小於等於 10 的情況下能有效減少座標範圍同時保留正確性。

- 最後在壓縮後的座標範圍上以 Dijkstra 求最少踩石子數（邊權為 0/1）。

注意：本模組著重在可讀性與在題目限制下（M<=100, T<=10）能夠運行。
若需更理論嚴謹的壓縮，可用 gcd 或 LCM 的方法確保餘類不變。
"""


def min_stones(L: int, S: int, T: int, stones: List[int]) -> int:
    """回傳最少需要踩到的石子數。

    參數：
    - L: 橋長
    - S, T: 最小與最大跳躍距離（S <= step <= T）
    - stones: 石子位置列表（起點與終點保證無石）
    """
    # 若沒有石子，必定不會踩到任何石子
    if not stones:
        return 0

    # 若跳距固定（S == T），落點為 0,S,2S,...，直接檢查這些點是否為石子即可
    if S == T:
        step = S
        count = 0
        stone_set = set(stones)
        pos = step
        while pos < L:
            if pos in stone_set:
                count += 1
            pos += step
        return count

    # 先排序石子位置
    stones_sorted = sorted(stones)

    # 嘗試將長距離段落縮短來壓縮座標空間
    new_positions = []
    shift = 0  # 總共左移的量
    prev = 0
    L2 = L

    # threshold 用於決定何時壓縮：採保守值可在常見參數下減少錯誤
    #（在此題 S,T <= 10，使用 90 足以在測資上處理並降低狀態空間）
    threshold = 90

    for p in stones_sorted:
        # p - shift 為目前石子在壓縮後座標的暫時計算值
        gap = p - shift - prev
        if gap > threshold:
            # 若 gap 過大，就把後續座標左移 gap - threshold
            # 同時調整終點 L2
            delta_shrink = gap - threshold
            shift += delta_shrink
            L2 -= delta_shrink
        p_shifted = p - shift
        new_positions.append(p_shifted)
        prev = p_shifted

    # 最後處理終點與最後一顆石子的 gap
    final_gap = L2 - prev
    if final_gap > threshold:
        delta_shrink = final_gap - threshold
        L2 -= delta_shrink

    # 壓縮後的最大位置（視為終點）
    max_pos = L2

    # 石子集合（壓縮後座標）
    stone_set = set(new_positions)

    # 使用 Dijkstra（0/1 權重）計算最少踩石子數
    INF = 10**9
    dist = [INF] * (max_pos + 1)
    pq = [(0, 0)]
    dist[0] = 0
    best_finish = INF

    while pq:
        cost, pos = heapq.heappop(pq)
        # 若此狀態不是目前最佳，跳過
        if cost > dist[pos]:
            continue

        for step in range(S, T + 1):
            newpos = pos + step
            # 若跳到或越過終點，視為成功
            if newpos >= max_pos:
                if cost < best_finish:
                    best_finish = cost
                continue

            # 落點若為石子，cost +1；否則 cost 不變
            add = 1 if newpos in stone_set else 0
            if cost + add < dist[newpos]:
                dist[newpos] = cost + add
                heapq.heappush(pq, (dist[newpos], newpos))

    return best_finish



if __name__ == '__main__':
    # 簡單示範：若要測試可修改下列變數後執行
    L = 20
    S = 2
    T = 3
    stones = [4, 5, 11, 12]
    print(min_stones(L, S, T, stones))
