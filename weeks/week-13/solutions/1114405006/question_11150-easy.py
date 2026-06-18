"""
簡易版：UVA 11150 — 最少踩石子（-easy）

說明（繁體中文）

目的：提供一個直觀且容易理解的實作來解題，方便教學或用於小型輸入。

題意回顧：青蛙從位置 0 開始跳，目標是跳到位置 >= L 即過河；每次跳距可以選 S..T 的整數值。
若落在石子位置則算踩到一顆石子。求過河時踩到石子的最小數量。

直觀演算法：
- 將每個整數座標視為節點；從 pos 可以走到 pos+step（step = S..T）。
- 如果落點是石子，該移動的代價為 1，否則為 0。
- 當 newpos >= L 時視為成功過河，更新最小踩石子數。
- 由於邊權重只有 0 或 1，可用 Dijkstra（或 0-1 BFS）求最短路；此檔以 Dijkstra 實作以保持直觀。

限制與備註：
- 此簡易版會在座標空間做直接探索，當 L 很大（如 1e9）時會非常慢且耗記憶體，僅建議用於小型測資或教學。
- 真正處理大 L 的版本需採用座標壓縮或其他優化策略。

用法範例：
- 在 Python 中可用 importlib 動態載入此檔，或直接在同一目錄以 python 執行。

"""

from typing import List
import heapq


def min_stones_easy(L: int, S: int, T: int, stones: List[int]) -> int:
    """
    簡易直觀實作（暴力版）。

    參數：
    - L: 過河門檻（目標位置，當位置 >= L 則視為過河）
    - S, T: 每次跳躍距離的最小值與最大值（包含端點）
    - stones: 石子的座標列表

    回傳：最少踩到的石子數；若理論上無法過河則回傳 -1（題目通常保證可過河）。
    """
    stone_set = set(stones)

    INF = 10**9

    # 使用 dict 儲存被探索過的位置到達的最小踩石子數，節省記憶體
    dist = {0: 0}
    pq = [(0, 0)]  # (cost, pos)
    best_finish = INF

    # Dijkstra 主迴圈；由於權重只有 0/1，也可改用 0-1 BFS
    while pq:
        cost, pos = heapq.heappop(pq)
        # 若此狀態不是目前的最小值則跳過
        if cost != dist.get(pos, INF):
            continue

        # 嘗試所有可能的跳躍距離
        for step in range(S, T + 1):
            newpos = pos + step

            # 若超過或到達目標，更新 best_finish
            if newpos >= L:
                if cost < best_finish:
                    best_finish = cost
                continue

            # 落在石子上則要加 1
            add = 1 if newpos in stone_set else 0
            newcost = cost + add

            # 若找到更小成本則更新並加入佇列
            if newcost < dist.get(newpos, INF):
                dist[newpos] = newcost
                heapq.heappush(pq, (newcost, newpos))

    return best_finish if best_finish != INF else -1


if __name__ == '__main__':
    # 小範例測試
    L = 20
    S = 2
    T = 3
    stones = [4, 5, 11, 12]
    print('min_stones_easy:', min_stones_easy(L, S, T, stones))
